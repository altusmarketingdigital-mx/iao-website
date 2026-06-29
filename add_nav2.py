import os
import glob

html_files = glob.glob('*.html') + glob.glob('en/*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    prefix = '../' if ('en/' in filepath or 'en\\' in filepath) else ''
    
    # Desktop nav
    target_es = f'<a href="{prefix}blog-corrida-financiera.html" class="block px-6 py-2 text-sm font-semibold hover:text-brand-orange transition">Corrida Financiera Personalizada</a>'
    target_es_active = f'<a href="{prefix}blog-corrida-financiera.html" class="block px-6 py-2 text-sm font-semibold text-brand-orange transition">Corrida Financiera Personalizada</a>'
    
    new_link_es = f'\n                        <a href="{prefix}blog-optimiza-caldera.html" class="block px-6 py-2 text-sm font-semibold hover:text-brand-orange transition">Optimiza tu caldera infografía</a>'
    
    if target_es in content and new_link_es not in content:
        content = content.replace(target_es, target_es + new_link_es)
    
    if target_es_active in content and new_link_es not in content:
        content = content.replace(target_es_active, target_es_active + new_link_es)

    # Mobile nav
    mobile_es = f'<a href="{prefix}blog-corrida-financiera.html" class="text-2xl font-black text-brand-orange uppercase tracking-tighter hover:text-white transition-colors">Blog: Corrida Financiera</a>'
    new_mobile_es = f'\n            <a href="{prefix}blog-optimiza-caldera.html" class="text-2xl font-black text-brand-orange uppercase tracking-tighter hover:text-white transition-colors">Blog: Optimiza tu Caldera</a>'
    
    if mobile_es in content and new_mobile_es not in content:
        content = content.replace(mobile_es, mobile_es + new_mobile_es)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
