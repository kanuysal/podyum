import re
import os

def find_assets():
    with open('index.48ab324d.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Try different patterns
    patterns = [
        r'assets/[\w\./-]+\.\w+',
        r'\"[a-zA-Z0-9_\-\./]+\.(?:buf|json|webp|png|jpg|glb|gltf|bin|mp3)\"',
        r'\'[a-zA-Z0-9_\-\./]+\.(?:buf|json|webp|png|jpg|glb|gltf|bin|mp3)\''
    ]
    
    all_matches = set()
    js_files = ['index.48ab324d.js', 'assets/index.f4419199.js', 'widgets.js']
    for js_file in js_files:
        if not os.path.exists(js_file):
            continue
        with open(js_file, 'r', encoding='utf-8') as f:
            content = f.read()
        for p in patterns:
            matches = re.findall(p, content)
            for m in matches:
                all_matches.add(m.strip("'\""))
            
    with open('all_possible_assets.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted(all_matches)))

if __name__ == "__main__":
    find_assets()
