const fs = require('fs');
const path = require('path');

const dir = '.';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));
const enDir = './en';
let enFiles = [];
if (fs.existsSync(enDir)) {
    enFiles = fs.readdirSync(enDir).filter(f => f.endsWith('.html')).map(f => path.join(enDir, f));
}
const allFiles = [...files, ...enFiles];

const esReplace = `                <div class="nav-item h-full flex items-center relative group">
                    <a href="#" class="nav-link flex items-center gap-1">Blog <i class="fas fa-chevron-down text-[10px] opacity-60"></i></a>
                    <div class="absolute top-[100px] left-0 w-[260px] bg-white shadow-xl py-4 border-t-2 border-brand-orange opacity-0 invisible group-hover:opacity-100 group-hover:visible translate-y-2 group-hover:translate-y-0 transition-all duration-300 z-[100]">
                        <a href="{prefix}blog-checklist.html" class="block px-6 py-2 text-sm font-semibold hover:text-brand-orange transition">Checklist de Mantenimiento</a>
                    </div>
                </div>`;

const enReplace = `                <div class="nav-item h-full flex items-center relative group">
                    <a href="#" class="nav-link flex items-center gap-1">Blog <i class="fas fa-chevron-down text-[10px] opacity-60"></i></a>
                    <div class="absolute top-[100px] left-0 w-[260px] bg-white shadow-xl py-4 border-t-2 border-brand-orange opacity-0 invisible group-hover:opacity-100 group-hover:visible translate-y-2 group-hover:translate-y-0 transition-all duration-300 z-[100]">
                        <a href="{prefix}blog-checklist.html" class="block px-6 py-2 text-sm font-semibold hover:text-brand-orange transition">Maintenance Checklist</a>
                    </div>
                </div>`;

for (const file of allFiles) {
    let content = fs.readFileSync(file, 'utf8');
    const isEn = file.startsWith('en\\') || file.startsWith('en/');
    const prefix = isEn ? '../' : '';
    
    // Pattern 1: exactly like index.html 
    const p1 = `                <div class="nav-item h-full flex items-center relative group">\n                    <a href="#" class="nav-link flex items-center gap-1">Blog <i class="fas fa-chevron-down text-[10px] opacity-60"></i></a>\n                </div>`;
    
    // Pattern 2: without chevron
    const p2 = `                <div class="nav-item h-full flex items-center">\n                    <a href="#" class="nav-link">Blog</a>\n                </div>`;

    let replaced = content;
    const replacement = isEn ? enReplace.replace('{prefix}', prefix) : esReplace.replace('{prefix}', prefix);

    if (replaced.includes(p1)) {
        replaced = replaced.replace(p1, replacement);
    } else if (replaced.includes(p2)) {
        replaced = replaced.replace(p2, replacement);
    }

    if (content !== replaced) {
        fs.writeFileSync(file, replaced);
        console.log(`Updated ${file}`);
    }
}
