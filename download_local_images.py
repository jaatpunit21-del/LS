import urllib.request
import os
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Create images folder in workspace
output_dir = "c:/Users/jaatp/OneDrive/Desktop/cafe demo USA/images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Mapping of local filename to Unsplash CDN photo ID
image_map = {
    "hero_bg.jpg": "1588608368947-c243aea32bff",         # Garden lawn path (Hero)
    "about_main.jpg": "1527359443443-84a48aec73d2",      # Manicured garden lawn
    "about_accent.jpg": "1507591064344-4c6ce005b128",    # Beautiful lawn & path (instead of gardener hands)
    "before.jpg": "1595855759920-86582396756a",          # Soil texture (Before)
    "after.jpg": "1560749003-f4b1e17e2dff",           # Lush backyard green lawn (After)
    "portfolio_1.jpg": "1507591064344-4c6ce005b128",     # Beautiful garden path & lawn
    "portfolio_2.jpg": "1588608368947-c243aea32bff",     # Lush garden path
    "portfolio_3.jpg": "1560749003-f4b1e17e2dff",     # Cozy backyard lawn
    "portfolio_4.jpg": "1582268611958-ebfd161ef9cf",     # Miami luxury turf/lawn (instead of plant details)
    "portfolio_5.jpg": "1527359443443-84a48aec73d2",     # Pristine green lawn
    "portfolio_6.jpg": "1560749003-f4b1e17e2dff"      # Lush green lawn (working ID)
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

print("Starting download of local landscaping images...")
for filename, pid in image_map.items():
    w_size = 1600 if filename in ["hero_bg.jpg", "before.jpg", "after.jpg"] else 800
    url = f"https://images.unsplash.com/photo-{pid}?w={w_size}&q=80"
    dest_path = os.path.join(output_dir, filename)
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx) as response:
            with open(dest_path, "wb") as f:
                f.write(response.read())
            print(f"Downloaded {filename} from ID {pid} (Size: {os.path.getsize(dest_path)} bytes)")
    except Exception as e:
        print(f"Failed to download {filename} from ID {pid}: {e}")

print("Image download process completed.")
