import os
import glob
import re

os.chdir('C:/Users/nk/.gemini/antigravity/scratch/drink-cocktail-menu')

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Colors
    # Richer black: #050505
    content = re.sub(r'"background-dark":\s*"#[0-9a-fA-F]+"', '"background-dark": "#050505"', content)
    # Warmer/more prominent gold: #eab308
    content = re.sub(r'"primary":\s*"#[0-9a-fA-F]+"', '"primary": "#eab308"', content)

    # Some hardcoded slate-900 backgrounds -> zinc-950 for richer black
    content = content.replace("bg-slate-900", "bg-zinc-950")
    
    # Headings
    content = content.replace('text-5xl md:text-7xl', 'text-6xl md:text-8xl')
    content = content.replace('text-5xl', 'text-6xl')
    content = content.replace('text-3xl', 'text-4xl')
    content = content.replace('text-2xl', 'text-3xl')
    
    # Spacing / Breathing room
    content = content.replace('py-12 md:py-20', 'py-16 md:py-24')
    content = content.replace('py-32', 'py-40 md:py-48')
    content = content.replace('mb-20', 'mb-28')
    content = content.replace('mb-12', 'mb-16')
    content = content.replace('gap-12', 'gap-16')
    
    # Menu Items Scannability & Contrast
    # Targeting <div class="flex gap-6 group">
    content = content.replace('class="flex gap-6 group"', 'class="flex gap-6 group p-5 -mx-5 hover:bg-white/5 rounded-2xl transition-all duration-300 border border-transparent hover:border-white/10"')
    # Targeting list items in classics
    content = content.replace('class="flex justify-between items-center group cursor-default"', 'class="flex justify-between items-center group cursor-default p-5 -mx-5 hover:bg-white/5 rounded-2xl transition-all duration-300 border border-transparent hover:border-white/10"')
    
    # Text contrast for menu item descriptions
    content = content.replace('text-slate-400 text-sm italic mb-1', 'text-slate-300 text-base italic mb-2')
    content = content.replace('text-slate-400 text-sm italic leading-relaxed', 'text-slate-300 text-base italic leading-relaxed')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for html_file in glob.glob('*.html'):
    update_file(html_file)
    print(f"Updated {html_file}")
