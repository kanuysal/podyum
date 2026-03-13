
import os

filepath = r"d:\minadesign\elements\defile\index.48ab324d.js"
with open(filepath, 'rb') as f:
    content = f.read()
    
target = b"new Preloader"
pos = content.find(target)

if pos != -1:
    print(f"Found {target} at {pos}")
    start = max(0, pos - 100)
    end = min(len(content), pos + 100)
    print(content[start:end].decode('utf-8', errors='ignore'))
else:
    print("Not found")
