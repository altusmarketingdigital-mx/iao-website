import glob
import re

html_files = glob.glob('*.html') + glob.glob('en/*.html')
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    prefix = '../' if ('en/' in filepath or 'en\\' in filepath) else ''
    new_link = f'{prefix}reformas.html'
    
    # Replace dropdown link
    content = re.sub(r'<a href=\"[^\"]*\" class=\"block px-6 py-2 text-sm font-semibold hover:text-brand-orange transition\">Reformas</a>', 
                     f'<a href=\"{new_link}\" class=\"block px-6 py-2 text-sm font-semibold hover:text-brand-orange transition\">Reformas</a>', content)
                     
    # Replace mobile link
    content = re.sub(r'<a href=\"[^\"]*\" class=\"text-lg font-bold text-gray-300 hover:text-white transition-colors\">Reformas</a>', 
                     f'<a href=\"{new_link}\" class=\"text-lg font-bold text-gray-300 hover:text-white transition-colors\">Reformas</a>', content)
                     
    # Replace special case in servicio-auditoria-cfd.html
    content = re.sub(r'<a href=\"[^\"]*\" class=\"block px-6 py-2 text-sm font-semibold text-brand-orange transition\">Reformas</a>', 
                     f'<a href=\"{new_link}\" class=\"block px-6 py-2 text-sm font-semibold text-brand-orange transition\">Reformas</a>', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Navigation updated.')
