#!/bin/bash

# Exit on error
set -e

echo "🚀 Starting build process for Net Speed Monitor..."

# 1. Clean previous builds
echo "🧹 Cleaning old build files..."
rm -rf build dist

# 2. Build the app
echo "📦 Building .app bundle with py2app..."
python3 setup.py py2app

# 3. Create a ZIP of the app
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
