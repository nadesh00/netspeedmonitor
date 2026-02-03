#!/usr/bin/env python3
"""
Network Speed Monitor for macOS
Displays real-time upload/download speed in the menu bar
"""

import rumps
import psutil
import time


class NetSpeedMonitor(rumps.App):
    def __init__(self):
        super(NetSpeedMonitor, self).__init__("📡", quit_button=None)
        counters = psutil.net_io_counters()
        self.last_bytes_recv = counters.bytes_recv
        self.last_bytes_sent = counters.bytes_sent
        self.last_check_time = time.time()
        self.speed_menu_item = rumps.MenuItem("Current Speed: Calculating...", callback=None)

        # Menu items
        self.menu = [
            self.speed_menu_item,
            rumps.separator,
            rumps.MenuItem("Update Interval"),
            rumps.MenuItem("1 second", callback=self.set_interval_1s),
            rumps.MenuItem("2 seconds", callback=self.set_interval_2s),
            rumps.MenuItem("5 seconds", callback=self.set_interval_5s),
            rumps.separator,
            rumps.MenuItem("About", callback=self.show_about),
            rumps.MenuItem("Quit", callback=self.quit_app)
        ]

        # Start timer on main thread
        self.timer = rumps.Timer(self.monitor_speed, 1)
        self.timer.start()

    def monitor_speed(self, _):
        """Monitor network speed - called by timer on main thread"""
        current_time = time.time()
        counters = psutil.net_io_counters()
        current_recv = counters.bytes_recv
        current_sent = counters.bytes_sent

        # Calculate speed
        time_elapsed = current_time - self.last_check_time
        recv_diff = current_recv - self.last_bytes_recv
        sent_diff = current_sent - self.last_bytes_sent

        if time_elapsed > 0:
            down_bps = recv_diff / time_elapsed
            up_bps = sent_diff / time_elapsed
            
            # Determine which speed to show (Priority: Upload if > Download, else Download)
            if up_bps > down_bps:
                display_bps = up_bps
                prefix = "↑"
                mode = "Upload"
            else:
                display_bps = down_bps
                prefix = "↓"
                mode = "Download"

            speed_text = self.format_speed(display_bps)

            # Update menu bar title (using mono-spaced formatting in format_speed)
            self.title = f"{prefix} {speed_text}"

            # Update menu item with details
            self.speed_menu_item.title = f"{mode}: {speed_text}"

        # Update for next iteration
        self.last_bytes_recv = current_recv
        self.last_bytes_sent = current_sent
        self.last_check_time = current_time
    
    def format_speed(self, bytes_per_second):
        """Format speed with fixed width, starting at KB/s (no B/s)"""
        # Logic: Always produce a string of consistent length
        if bytes_per_second < 1024 * 1024:
            # "   0.5 KB/s" to " 999.9 KB/s"
            # We treat everything under 1MB as KB
            return f"{bytes_per_second / 1024:>5.1f} KB/s"
        elif bytes_per_second < 1024 * 1024 * 1024:
            # "  12.4 MB/s"
            return f"{bytes_per_second / (1024 * 1024):>5.1f} MB/s"
        else:
            # "   1.2 GB/s"
            return f"{bytes_per_second / (1024 * 1024 * 1024):>5.1f} GB/s"
    
    def set_interval_1s(self, _):
        """Set update interval to 1 second"""
        self.timer.interval = 1
        rumps.notification("Net Speed Monitor", "Update Interval", "Set to 1 second")

    def set_interval_2s(self, _):
        """Set update interval to 2 seconds"""
        self.timer.interval = 2
        rumps.notification("Net Speed Monitor", "Update Interval", "Set to 2 seconds")

    def set_interval_5s(self, _):
        """Set update interval to 5 seconds"""
        self.timer.interval = 5
        rumps.notification("Net Speed Monitor", "Update Interval", "Set to 5 seconds")
    
    def show_about(self, _):
        """Show about dialog"""
        rumps.alert(
            title="Net Speed Monitor",
            message="Version 1.1\n\nSmart upload/download switching\nwith fixed-width numerals."
        )
    
    def quit_app(self, _):
        """Quit the application"""
        self.timer.stop()
        rumps.quit_application()


if __name__ == "__main__":
    NetSpeedMonitor().run()
