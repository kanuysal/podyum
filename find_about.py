
import os

filepath = r"d:\minadesign\elements\defile\index.48ab324d.js"
with open(filepath, 'rb') as f:
    content = f.read()
    
target = b".header-more--about"
pos = content.find(target)

if pos != -1:
    print(f"Found {target} at {pos}")
    start = max(0, pos - 500)
    end = min(len(content), pos + 1000)
    print(content[start:end].decode('utf-8', errors='ignore'))
else:
    print("Not found")
