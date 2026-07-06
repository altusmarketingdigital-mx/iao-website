import sys

filename = 'blog-checklist.html'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Update image name
content = content.replace('step1_quemador.png', 'revision_quemador.JPG')

# Change object-cover to object-contain
content = content.replace('object-cover transform group-hover:scale-110', 'object-contain transform group-hover:scale-110')

# Remove gray overlay
target = '<div class="absolute inset-0 bg-brand-dark/20 group-hover:bg-transparent transition-colors duration-500 z-10"></div>'
content = content.replace(target, '')

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)
