
import os

filepath = r"d:\minadesign\elements\defile\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix favicons
old_favicon = '<link rel="apple-touch-icon" sizes="180x180" href="assets/textures/logo.ico"><link rel="icon" type="image/x-icon" href="assets/textures/logo.ico"><link rel="shortcut icon" href="assets/textures/logo.ico">'
new_favicon = '<link rel="icon" type="image/x-icon" href="assets/textures/logo.ico"><link rel="shortcut icon" href="assets/textures/logo.ico"><link rel="apple-touch-icon" href="assets/textures/logo.ico">'
content = content.replace(old_favicon, new_favicon)

# Add Skip Button logic
# Find where the preloader explanation ends
target = 'id="preloader-explanation">Defile hazırlanıyor</p></div>'
replacement = target + '<div id="skip-preloader" style="display:none; cursor:pointer; margin-top:20px; font-family: sans-serif; color:white; border:1px solid white; padding:10px 20px; border-radius:30px; font-size:12px; letter-spacing:1px; z-index:100; position:relative;">GİRİŞ YAP (Sıkışırsa Tıklayın)</div>'
content = content.replace(target, replacement)

# Add Script to show skip button and handle force start
script_to_add = """
<script>
  setTimeout(function() {
    var btn = document.getElementById('skip-preloader');
    if (btn) btn.style.display = 'inline-block';
    if (btn) btn.onclick = function() {
      var preloader = document.getElementById('page--preloader');
      if (preloader) preloader.classList.remove('is-active');
      if (window.properties) window.properties.isPreloaderFinished = true;
    };
  }, 10000);
</script>
"""
content = content.replace('</body>', script_to_add + '</body>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html")
