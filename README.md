# 📡 Net Speed Monitor for macOS

A lightweight, premium network speed monitor for your macOS menu bar. Track your real-time upload and download speeds with a clean, minimalist interface.

![Version](https://img.shields.io/badge/version-1.1.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![macOS](https://img.shields.io/badge/platform-macOS-black.svg)

## ✨ Features

- **Smart Switching**: Automatically displays whichever speed is currently higher (Upload or Download).
- **Clean UI**: Minimalist menu bar display with mono-spaced formatting for consistent layout.
- **Customizable Intervals**: Choose between 1, 2, or 5-second update frequencies.
- **Lightweight**: Built with Python and optimized for low resource consumption.
- **No Dock Icon**: Runs as a pure menu bar app for a clutter-free experience.

## 🚀 Installation

### Option 1: Download the App (Recommended)
1. Go to the [Rereleases](https://github.com/YOUR_USERNAME/netspeedmonitor/releases) page.
2. Download the latest `NetSpeedMonitor.dmg` or `NetSpeedMonitor.app.zip`.
3. Drag `NetSpeedMonitor.app` to your Applications folder.
4. Open the app. (You may need to right-click and select "Open" for the first time due to macOS security settings).

### Option 2: Run from Source
If you prefer to run from source, you'll need Python 3 installed:

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/netspeedmonitor.git
cd netspeedmonitor

# Install dependencies
pip install -r requirements.txt

# Run the app
python3 net_speed_monitor.py
```

## 🛠 Building for macOS
To build your own `.app` bundle:
```bash
python3 setup.py py2app
```
The compiled app will be in the `dist/` directory.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments
- Inspired by the need for a simple, non-intrusive speed monitor.
- Built with [rumps](https://github.com/jaredks/rumps) and [psutil](https://github.com/giampaolo/psutil).
