from setuptools import setup

APP = ['net_speed_monitor.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'app_icon.icns',
    'plist': {
        'LSUIElement': True,  # This makes it a menu-bar only app (no dock icon)
        'CFBundleName': "NetSpeedMonitor",
        'CFBundleDisplayName': "Net Speed Monitor",
        'CFBundleGetInfoString': "Network Speed Monitor for macOS",
        'CFBundleIdentifier': "com.nadesh.netspeedmonitor",
        'CFBundleVersion': "1.1.0",
        'CFBundleShortVersionString': "1.1.0",
        'NSHumanReadableCopyright': u"Copyright © 2026, Nadesh, All Rights Reserved"
    },
    'packages': ['rumps', 'psutil'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
