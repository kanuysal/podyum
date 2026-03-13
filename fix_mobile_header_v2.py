
import os

filepath = r"d:\minadesign\elements\defile\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Refine the mobile header to avoid overlap
# We'll make the logo container pointer-events: none and the link pointer-events: auto
# Also ensure the header-more container is definitely on top

content = content.replace('style="display:inline-block; mix-blend-mode:difference; z-index:10; pointer-events:auto; padding:20px; width:fit-content;"', 
                         'style="display:inline-block; mix-blend-mode:difference; z-index:10; pointer-events:none; padding:20px; width:fit-content;"')

content = content.replace('<a href="https://minalidya.com"', '<a href="https://minalidya.com" style="pointer-events:auto;"')

# Update the style block to be even more aggressive for mobile
style_update = """
<style id="mobile-header-fix">
  @media screen and (max-width: 812px) {
    .logo-container h1 {
      font-size: 28px !important;
      letter-spacing: 2px !important;
      margin: 0 !important;
    }
    .logo-container {
      padding: 15px !important;
      max-width: 70vw !important;
      overflow: hidden !important;
    }
    .header-more {
      z-index: 9999 !important;
      pointer-events: auto !important;
      position: fixed !important;
      top: 15px !important;
      right: 15px !important;
      display: flex !important;
      opacity: 1 !important;
      visibility: visible !important;
    }
    .header-more--about {
      pointer-events: auto !important;
    }
  }
</style>
"""

# Replace the previous style block if it exists
if '<style>' in content and '@media screen and (max-width: 812px)' in content:
    import re
    content = re.sub(r'<style>.*?</style>', style_update, content, flags=re.DOTALL)
else:
    content = content.replace('</head>', style_update + '</head>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html with aggressive mobile header fixes")
