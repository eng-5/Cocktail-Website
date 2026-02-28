import os

os.chdir('C:/Users/nk/.gemini/antigravity/scratch/drink-cocktail-menu')

style_and_script = """
<style>
    .reveal-on-scroll {
        opacity: 0;
        transform: translateY(2rem);
        transition: opacity 1.2s cubic-bezier(0.16, 1, 0.3, 1), transform 1.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .reveal-on-scroll.is-visible {
        opacity: 1;
        transform: translateY(0);
    }
</style>
<script>
    document.addEventListener("DOMContentLoaded", function() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });
        
        document.querySelectorAll('.reveal-on-scroll').forEach((el) => {
            observer.observe(el);
        });
    });
</script>
</body>
"""

files = ['index.html', 'menu.html', 'events.html']

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "reveal-on-scroll" not in content:
        # replace </body>
        content = content.replace('</body>', style_and_script)
        
        # Add reveal-on-scroll to key elements
        # index.html
        content = content.replace('class="max-w-[900px] pt-20"', 'class="max-w-[900px] pt-20 reveal-on-scroll"')
        content = content.replace('class="space-y-10"', 'class="space-y-10 reveal-on-scroll"')
        content = content.replace('class="group cursor-pointer"', 'class="group cursor-pointer reveal-on-scroll"')
        content = content.replace('class="flex flex-col items-center text-center space-y-6 px-4"', 'class="flex flex-col items-center text-center space-y-6 px-4 reveal-on-scroll"')
        
        # menu.html
        content = content.replace('class="w-full max-w-6xl px-4 py-16 md:py-24"', 'class="w-full max-w-6xl px-4 py-16 md:py-24 reveal-on-scroll"')
        content = content.replace('class="flex gap-6 group p-5 -mx-5 hover:bg-white/5 rounded-2xl transition-all duration-300 border border-transparent hover:border-white/10"', 'class="flex gap-6 group p-5 -mx-5 hover:bg-white/5 rounded-2xl transition-all duration-300 border border-transparent hover:border-white/10 reveal-on-scroll"')
        content = content.replace('class="flex justify-between items-center group cursor-default p-5 -mx-5 hover:bg-white/5 rounded-2xl transition-all duration-300 border border-transparent hover:border-white/10"', 'class="flex justify-between items-center group cursor-default p-5 -mx-5 hover:bg-white/5 rounded-2xl transition-all duration-300 border border-transparent hover:border-white/10 reveal-on-scroll"')
        content = content.replace('class="bg-primary/5 rounded-2xl border border-primary/20 p-8 md:p-12 text-center mb-28"', 'class="bg-primary/5 rounded-2xl border border-primary/20 p-8 md:p-12 text-center mb-28 reveal-on-scroll"')
        
        # events.html
        content = content.replace('class="absolute bottom-0 left-0 p-10 z-20"', 'class="absolute bottom-0 left-0 p-10 z-20 reveal-on-scroll"')
        content = content.replace('class="bg-background-dark border border-primary/20 rounded-2xl overflow-hidden shadow-2xl"', 'class="bg-background-dark border border-primary/20 rounded-2xl overflow-hidden shadow-2xl reveal-on-scroll"')
        content = content.replace('class="mt-20 flex flex-col md:flex-row gap-16 items-center"', 'class="mt-20 flex flex-col md:flex-row gap-16 items-center reveal-on-scroll"')
        
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(content)

print(f"Added animations to files.")
