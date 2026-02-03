#!/bin/bash

# Exit on error
set -e

echo "🚀 Starting build process for Net Speed Monitor..."

# 1. Clean previous builds
echo "🧹 Cleaning old build files..."
rm -rf build dist

# 2. Build the app
echo "📦 Building .app bundle with PyInstaller..."
pyinstaller --noconfirm --onefile --windowed --icon "app_icon.icns" --name "NetSpeedMonitor" --hidden-import "rumps" --hidden-import "psutil" net_speed_monitor.py

# 3. Ad-hoc Signing
echo "✍️  Applying ad-hoc signature..."
codesign --force --deep --sign - dist/NetSpeedMonitor.app

# 4. Create a ZIP of the app
echo "🤐 Zipping the app for distribution..."
cd dist
zip -r NetSpeedMonitor.app.zip NetSpeedMonitor.app
cd ..

echo "✅ Build complete! You can find the release files in the 'dist' folder:"
echo "   - dist/NetSpeedMonitor.app (Ready to use)"
echo "   - dist/NetSpeedMonitor.app.zip (Ready to upload to GitHub)"

# Optional: Suggest tagging
echo ""
echo "💡 To release on GitHub, run:"
echo "   git tag -a v1.0.0 -m \"Release v1.0.0\""
echo "   git push origin main --tags"
