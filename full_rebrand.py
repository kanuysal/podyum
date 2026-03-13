import re
import os

def full_rebrand():
    # 1. index.htm Branding
    with open('index.htm', 'r', encoding='utf-8') as f:
        htm = f.read()

    # Logo
    logo_pattern = r'<div class="header-item--lab">.*?</div>'
    new_logo = '<div class="header-item--lab"><a href="https://minalidya.com" target="_blank"><img src="assets/textures/mllogogenis.png" style="height: 45px;" /></a></div>'
    htm = re.sub(logo_pattern, new_logo, htm, flags=re.DOTALL)

    # Footer Labels Revert
    htm = htm.replace('<p>Mina Lidya Gelinlik</p>', '<p>Camera view</p>')
    htm = htm.replace('<p>Mina Lidya Nişanlık</p>', '<p>Free view</p>')
    htm = htm.replace('<p>Mina Lidya Nisanlik</p>', '<p>Free view</p>')
    htm = htm.replace('<p>Mina Lidya Kina</p>', '<p>Change led lights</p>')
    htm = htm.replace('<p>Mina Lidya Abiye</p>', '<p>Change led lights</p>')

    # About Content Turkish
    htm = htm.replace('lusion is an award winning mutlidisciplinary production studio.', 'MINA LIDYA COUTURE - SİZ HAYAL EDİN, BİZ TASARLAYALIM')
    htm = htm.replace('From creative to production, we collaborate with creative agencies and design studios to deliver compelling, real-time experiences, which go far beyond expectations.', 'Online Couture hizmetimizle, gelinliğinizin her detayını kişiselleştirme fırsatına sahip olacak, Mina Lidya Couture koleksiyonunu tanımlayan zarafet ve kadınsılığı kucaklayacaksınız.')
    
    # Simple replace for common Lusion strings in htm
    htm = htm.replace('created by Lusion', 'created by Mina Lidya')
    htm = htm.replace('Lusion', 'Mina Lidya')

    with open('index.htm', 'w', encoding='utf-8') as f:
        f.write(htm)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(htm)

    # 2. JS Branding
    js_path = 'index.48ab324d.js'
    with open(js_path, 'r', encoding='utf-8') as f:
        js = f.read()
    js = js.replace('made with ❤️ by Lusion', 'made with ❤️ by Mina Lidya')
    js = js.replace('Infinite Passerella - Lusion', 'Mina Lidya Couture')
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js)

    # 3. JSON Branding
    json_path = 'assets/data/colornames_new.json'
    with open(json_path, 'r', encoding='utf-8') as f:
        jsn = f.read()
    jsn = jsn.replace('Amber Wave', 'Mina Lidya Couture')
    jsn = jsn.replace('Lusion', 'Mina Lidya')
    with open(json_path, 'w', encoding='utf-8') as f:
        f.write(jsn)

if __name__ == "__main__":
    full_rebrand()
    print("Full rebrand script executed successfully.")
