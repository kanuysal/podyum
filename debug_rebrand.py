import re
import os

def check_and_replace():
    path = 'index.htm'
    print(f"Reading {path}...")
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Header Logo
    svg_pattern = r'<div class="header-item--lab">.*?</div>'
    new_logo = '<div class="header-item--lab"><a href="https://minalidya.com" target="_blank"><img src="assets/textures/mllogogenis.png" style="height: 45px;" /></a></div>'
    if re.search(svg_pattern, content, re.DOTALL):
        print("Found logo SVG, replacing...")
        content = re.sub(svg_pattern, new_logo, content, flags=re.DOTALL)
    else:
        print("Logo SVG not found with regex.")

    # 2. Footer
    if '<p>Mina Lidya Gelinlik</p>' in content:
        print("Found Gelinlik label, reverting...")
        content = content.replace('<p>Mina Lidya Gelinlik</p>', '<p>Camera view</p>')
    
    # 3. About
    if 'lusion is an award winning' in content:
        print("Found Lusion about text, replacing...")
        # (Shortened for the script to be safe)
        content = content.replace('lusion is an award winning mutlidisciplinary production studio.', 'MINA LIDYA COUTURE')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Write complete.")

if __name__ == "__main__":
    check_and_replace()
