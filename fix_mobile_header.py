
import os

filepath = r"d:\minadesign\elements\defile\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the header overlap
# We use a media query to shrink the logo on mobile and ensure the Hakkımızda button is reachable

old_header_start = '<header><div style="mix-blend-mode:difference; z-index:1000; pointer-events:auto; padding:20px;">'
new_header_start = '<header><div class="logo-container" style="display:inline-block; mix-blend-mode:difference; z-index:10; pointer-events:auto; padding:20px; width:fit-content;">'

content = content.replace(old_header_start, new_header_start)

# Add some CSS to the head to handle the logo on mobile and the button z-index
style_to_add = """
<style>
  @media screen and (max-width: 812px) {
    .logo-container h1 {
      font-size: 32px !important;
      letter-spacing: 3px !important;
    }
    .logo-container {
      padding: 10px !important;
    }
    .header-more {
      z-index: 1001 !important;
      pointer-events: auto !important;
    }
  }
</style>
"""

if '</head>' in content:
    content = content.replace('</head>', style_to_add + '</head>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html with mobile header fixes")
