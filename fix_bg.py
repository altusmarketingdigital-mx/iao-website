import sys

files = ['blog-optimiza-caldera.html', 'blog-corrida-financiera.html']
target = '<div class="absolute inset-0 bg-brand-dark/20 group-hover:bg-transparent transition-colors duration-500 z-10"></div>'

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = content.replace(target, '')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
