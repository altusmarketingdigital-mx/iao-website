import os
import glob

html_files = glob.glob('*.html') + glob.glob('en/*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    prefix = '../' if ('en/' in filepath or 'en\\' in filepath) else ''
    new_link_es = f'\n                        <a href="{prefix}blog-corrida-financiera.html" class="block px-6 py-2 text-sm font-semibold hover:text-brand-orange transition">Corrida Financiera Personalizada</a>'
    new_link_en = f'\n                        <a href="{prefix}blog-corrida-financiera.html" class="block px-6 py-2 text-sm font-semibold hover:text-brand-orange transition">Custom Financial Projection</a>'
    
    # We look for the Checklist link
    target_es = f'<a href="{prefix}blog-checklist.html" class="block px-6 py-2 text-sm font-semibold hover:text-brand-orange transition">Checklist de Mantenimiento</a>'
    target_en = f'<a href="{prefix}blog-checklist.html" class="block px-6 py-2 text-sm font-semibold hover:text-brand-orange transition">Maintenance Checklist</a>'

    if target_es in content and new_link_es not in content:
        content = content.replace(target_es, target_es + new_link_es)
    elif target_en in content and new_link_en not in content:
        content = content.replace(target_en, target_en + new_link_en)
        
    # Also update mobile menu links
    mobile_es = f'<a href="{prefix}blog-checklist.html" class="text-2xl font-black text-brand-orange uppercase tracking-tighter hover:text-white transition-colors">Blog: Checklist</a>'
    new_mobile_es = f'\n            <a href="{prefix}blog-corrida-financiera.html" class="text-2xl font-black text-brand-orange uppercase tracking-tighter hover:text-white transition-colors">Blog: Corrida Financiera</a>'
    
    if mobile_es in content and new_mobile_es not in content:
        content = content.replace(mobile_es, mobile_es + new_mobile_es)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
