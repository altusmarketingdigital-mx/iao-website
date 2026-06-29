import os
import re
import glob

def update_links():
    html_files = glob.glob('*.html')
    
    # Regex to match href="#" ... >Mantenimiento</a> or Digitalización de calderas</a>
    # We want to replace href="#" with href="construccion.html"
    
    pattern_mant = re.compile(r'href="#"([^>]*>\s*Mantenimiento\s*</a>)', re.IGNORECASE)
    pattern_digi = re.compile(r'href="#"([^>]*>\s*Digitalización de calderas\s*</a>)', re.IGNORECASE)
    
    for file in html_files:
        if file == 'construccion.html':
            continue
            
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = pattern_mant.sub(r'href="construccion.html"\1', content)
        new_content = pattern_digi.sub(r'href="construccion.html"\1', new_content)
        
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file}")

if __name__ == '__main__':
    update_links()
