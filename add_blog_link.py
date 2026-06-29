import os
import glob
import re

html_files = glob.glob('*.html')
# exclude ref.html and ref2.html
html_files = [f for f in html_files if not f.startswith('ref')]

def append_to_desktop(content, prefix=''):
    # Search for the desktop dropdown item
    # Since it depends on active/inactive, we can use regex to find where the "Optimiza tu caldera" link ends
    pattern1 = r'(<a href="{}blog-optimiza-caldera\.html"[^>]*>.*?</a>)'.format(prefix)
    
    if re.search(pattern1, content):
        def replacer1(match):
            original = match.group(1)
            # if the original has 'text-brand-orange' without hover:, it means it's the active page. But we just want to safely append.
            # actually better to just create the new link normally:
            new_link = f'\n                        <a href="{prefix}blog-reforma-calderas.html" class="block px-6 py-2 text-sm font-semibold hover:text-brand-orange transition">Reforma de Calderas de Biomasa</a>'
            return original + new_link
        content = re.sub(pattern1, replacer1, content)
    return content

def append_to_mobile(content, prefix=''):
    pattern2 = r'(<a href="{}blog-optimiza-caldera\.html"[^>]*>.*?</a>)'.format(prefix)
    # wait, the first regex might catch both if not careful.
    # desktop link has 'text-sm', mobile has 'text-2xl'
    
    # Actually, if we just do a sub for both occurrences, we'll append the same link type as what we captured?
    # No, better to match specific classes.
    pattern_desktop = r'(<a href="{}blog-optimiza-caldera\.html" class="block px-6 py-2[^>]*>.*?</a>)'.format(prefix)
    if re.search(pattern_desktop, content):
        def rep_desktop(m):
            new = f'\n                        <a href="{prefix}blog-reforma-calderas.html" class="block px-6 py-2 text-sm font-semibold hover:text-brand-orange transition">Reforma de Calderas de Biomasa</a>'
            return m.group(1) + new
        content = re.sub(pattern_desktop, rep_desktop, content)
        
    pattern_mobile = r'(<a href="{}blog-optimiza-caldera\.html" class="text-2xl[^>]*>.*?</a>)'.format(prefix)
    if re.search(pattern_mobile, content):
        def rep_mobile(m):
            new = f'\n            <a href="{prefix}blog-reforma-calderas.html" class="text-2xl font-black text-white uppercase tracking-tighter hover:text-brand-orange transition-colors">Blog: Reforma de Calderas de Biomasa</a>'
            return m.group(1) + new
        content = re.sub(pattern_mobile, rep_mobile, content)
    
    return content

for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    orig = content
    content = append_to_desktop(content)
    # Actually the append_to_desktop regex for pattern_desktop wouldn't match mobile because of class="block ...", 
    # so we combined them in the modified function above
    content = append_to_mobile(orig) 

    if content != orig:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {fname}")
    else:
        print(f"Skipped {fname}")
