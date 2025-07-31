#!/bin/bash

# Script to create favicon from Chris headshot
# Usage: ./create_favicon.sh path/to/your/headshot.png

if [ $# -eq 0 ]; then
    echo "Usage: $0 <path-to-headshot-image>"
    echo "Example: $0 ~/Downloads/chris-headshot.png"
    exit 1
fi

HEADSHOT="$1"
FAVICON_DIR="/Users/cp/code/blog/assets/favicons"

if [ ! -f "$HEADSHOT" ]; then
    echo "Error: File $HEADSHOT does not exist"
    exit 1
fi

echo "Creating favicon from $HEADSHOT..."

# Create different sizes for favicon
# Main favicon.ico (16x16, 32x32, 48x48 combined)
convert "$HEADSHOT" -resize 48x48 -gravity center -extent 48x48 /tmp/favicon-48.png
convert "$HEADSHOT" -resize 32x32 -gravity center -extent 32x32 /tmp/favicon-32.png  
convert "$HEADSHOT" -resize 16x16 -gravity center -extent 16x16 /tmp/favicon-16.png
convert /tmp/favicon-16.png /tmp/favicon-32.png /tmp/favicon-48.png "$FAVICON_DIR/favicon.ico"

# Standard favicon PNGs
convert "$HEADSHOT" -resize 16x16 -gravity center -extent 16x16 "$FAVICON_DIR/favicon-16x16.png"
convert "$HEADSHOT" -resize 32x32 -gravity center -extent 32x32 "$FAVICON_DIR/favicon-32x32.png"
convert "$HEADSHOT" -resize 96x96 -gravity center -extent 96x96 "$FAVICON_DIR/favicon-96x96.png"

# Apple touch icons
convert "$HEADSHOT" -resize 57x57 -gravity center -extent 57x57 "$FAVICON_DIR/apple-icon-57x57.png"
convert "$HEADSHOT" -resize 60x60 -gravity center -extent 60x60 "$FAVICON_DIR/apple-icon-60x60.png"
convert "$HEADSHOT" -resize 72x72 -gravity center -extent 72x72 "$FAVICON_DIR/apple-icon-72x72.png"
convert "$HEADSHOT" -resize 76x76 -gravity center -extent 76x76 "$FAVICON_DIR/apple-icon-76x76.png"
convert "$HEADSHOT" -resize 114x114 -gravity center -extent 114x114 "$FAVICON_DIR/apple-icon-114x114.png"
convert "$HEADSHOT" -resize 120x120 -gravity center -extent 120x120 "$FAVICON_DIR/apple-icon-120x120.png"
convert "$HEADSHOT" -resize 144x144 -gravity center -extent 144x144 "$FAVICON_DIR/apple-icon-144x144.png"
convert "$HEADSHOT" -resize 152x152 -gravity center -extent 152x152 "$FAVICON_DIR/apple-icon-152x152.png"
convert "$HEADSHOT" -resize 180x180 -gravity center -extent 180x180 "$FAVICON_DIR/apple-icon-180x180.png"

# Copy largest as precomposed
cp "$FAVICON_DIR/apple-icon-180x180.png" "$FAVICON_DIR/apple-icon-precomposed.png"
cp "$FAVICON_DIR/apple-icon-180x180.png" "$FAVICON_DIR/apple-icon.png"

# Android icons
convert "$HEADSHOT" -resize 36x36 -gravity center -extent 36x36 "$FAVICON_DIR/android-icon-36x36.png"
convert "$HEADSHOT" -resize 48x48 -gravity center -extent 48x48 "$FAVICON_DIR/android-icon-48x48.png"
convert "$HEADSHOT" -resize 72x72 -gravity center -extent 72x72 "$FAVICON_DIR/android-icon-72x72.png"
convert "$HEADSHOT" -resize 96x96 -gravity center -extent 96x96 "$FAVICON_DIR/android-icon-96x96.png"
convert "$HEADSHOT" -resize 144x144 -gravity center -extent 144x144 "$FAVICON_DIR/android-icon-144x144.png"
convert "$HEADSHOT" -resize 192x192 -gravity center -extent 192x192 "$FAVICON_DIR/android-icon-192x192.png"

# Microsoft icons
convert "$HEADSHOT" -resize 70x70 -gravity center -extent 70x70 "$FAVICON_DIR/ms-icon-70x70.png"
convert "$HEADSHOT" -resize 144x144 -gravity center -extent 144x144 "$FAVICON_DIR/ms-icon-144x144.png"
convert "$HEADSHOT" -resize 150x150 -gravity center -extent 150x150 "$FAVICON_DIR/ms-icon-150x150.png"
convert "$HEADSHOT" -resize 310x310 -gravity center -extent 310x310 "$FAVICON_DIR/ms-icon-310x310.png"

# Clean up temp files
rm -f /tmp/favicon-*.png

echo "✅ Favicon created successfully!"
echo "All favicon files have been updated in $FAVICON_DIR"
echo ""
echo "Your new personal favicon is ready to use!"