import re
import os

def run_fix():
    path = "index.html"
    if not os.path.exists(path):
        print("index.html not found")
        return

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Define the new aesthetic header
    # Large punto (62px), Italiana font, difference blend mode
    new_h = (
        '<header>'
        '<div style="mix-blend-mode:difference; z-index:1000; pointer-events:auto; padding:20px;">'
        '<a href="https://minalidya.com" target="_blank" style="text-decoration:none;">'
        '<h1 style="font-family:\'Italiana\', serif; font-size:62px; color:white; font-weight:bold; letter-spacing:6px; margin:0; line-height:1;">MİNA LİDYA</h1>'
        '</a>'
        '</div>'
        '<div class="header-more">'
        '<div class="header-more--audio"><div id="audio-btn" class="control__content link"><div class="audio__bar"></div><div class="audio__bar"></div><div class="audio__bar"></div><div class="audio__bar"></div></div></div>'
        '<div class="header-more--about"><h3>Hakkımızda</h3></div>'
        '</div>'
        '</header>'
    )

    # Use a non-greedy regex to find the header tag and its content
    # We match from <header to </header>
    pattern = re.compile(r'<header>.*?</header>', re.DOTALL)
    
    if pattern.search(content):
        updated_content = pattern.sub(new_h, content)
        with open(path, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print("index.html: Header updated.")
    else:
        print("index.html: <header> tag not found.")

    # Also sync to index.htm just in case
    if os.path.exists("index.htm"):
        with open("index.htm", "w", encoding="utf-8") as f:
            f.write(updated_content)
        print("index.htm: Synced.")

if __name__ == "__main__":
    run_fix()
