const fs = require('fs');
const path = require('path');

const dir = '.';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html') && f !== 'blog-checklist.html');
const enDir = './en';
let enFiles = [];
if (fs.existsSync(enDir)) {
    enFiles = fs.readdirSync(enDir).filter(f => f.endsWith('.html') && !f.includes('blog-')).map(f => path.join(enDir, f));
}
const allFiles = [...files, ...enFiles];

for (const file of allFiles) {
    let content = fs.readFileSync(file, 'utf8');
    const isEn = file.startsWith('en\\') || file.startsWith('en/');
    const prefix = isEn ? '../' : '';
    
    // Look for the end of the mobile menu
    const target = isEn ? `<a href="products.html" class="text-2xl font-black text-brand-orange uppercase tracking-tighter transition-colors">Products</a>` : `<a href="productos.html" class="text-2xl font-black text-brand-orange uppercase tracking-tighter transition-colors">Productos</a>`;
    const target2 = isEn ? `<a href="products.html" class="text-2xl font-black text-white uppercase tracking-tighter hover:text-brand-orange transition-colors">Products</a>` : `<a href="productos.html" class="text-2xl font-black text-white uppercase tracking-tighter hover:text-brand-orange transition-colors">Productos</a>`;

    const replacementEs = `\n            <a href="${prefix}blog-checklist.html" class="text-2xl font-black text-white uppercase tracking-tighter hover:text-brand-orange transition-colors">Blog: Checklist</a>`;
    const replacementEn = `\n            <a href="${prefix}blog-checklist.html" class="text-2xl font-black text-white uppercase tracking-tighter hover:text-brand-orange transition-colors">Blog: Checklist</a>`;

    let replaced = content;
    if (replaced.includes(target) && !replaced.includes('Blog: Checklist')) {
        replaced = replaced.replace(target, target + (isEn ? replacementEn : replacementEs));
    } else if (replaced.includes(target2) && !replaced.includes('Blog: Checklist')) {
        replaced = replaced.replace(target2, target2 + (isEn ? replacementEn : replacementEs));
    }

    if (content !== replaced) {
        fs.writeFileSync(file, replaced);
        console.log(`Updated mobile menu in ${file}`);
    }
}
