import re

with open('modeles/pista-hr.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hero text hide on mobile
# Find <div class="container mx-auto px-4 lg:px-8 relative z-10"> after <div class="absolute inset-0 bg-gradient-to-t...
# and replace it with hidden md:block
target_container = '<div class="container mx-auto px-4 lg:px-8 relative z-10">'
new_container = '<div class="container mx-auto px-4 lg:px-8 relative z-10 hidden md:block">'
content = content.replace(target_container, new_container, 1) # Only first occurrence

# 2. Add mobile text + buttons
mobile_buttons_old = """    <!-- ===== MOBILE BUTTONS (Under Video) ===== -->
    <div class="md:hidden flex justify-center gap-3 py-6 px-4 bg-black border-b border-gray-900">
        <a href="../devis.html" class="flex-1 text-center px-2 py-3 bg-kim-red text-white font-bold uppercase tracking-widest text-[10px] hover:bg-red-800 transition-colors">Demander un Devis</a>
        <a href="#fiche" class="flex-1 text-center px-2 py-3 border border-white/40 text-white font-bold uppercase tracking-widest text-[10px] hover:border-kim-red hover:text-kim-red transition-colors">Fiche Technique</a>
    </div>"""

mobile_text_buttons_new = """    <!-- ===== MOBILE TEXT + BUTTONS (Under Video) ===== -->
    <div class="md:hidden py-10 px-4 bg-kim-darker border-b border-gray-900 text-center flex flex-col items-center">
        <span class="inline-block text-kim-red font-bold tracking-[0.4em] uppercase text-[10px] mb-3">KIM Motors — Sport Urbain</span>
        <h1 class="text-7xl font-sport font-bold text-white leading-none mb-4 tracking-tight">PISTA <span class="text-kim-red">HR</span></h1>
        <p class="text-gray-400 text-xs mb-8 font-light max-w-sm">Le scooter qui redéfinit la mobilité urbaine. Un moteur 110CC vif, un freinage précis, et un design qui s'impose.</p>
        <div class="flex justify-center gap-2 w-full">
            <a href="../devis.html" class="flex-1 text-center px-2 py-3 bg-kim-red text-white font-bold uppercase tracking-widest text-[9px] sm:text-[10px] hover:bg-red-800 transition-colors whitespace-nowrap">Demander un Devis</a>
            <a href="#fiche" class="flex-1 text-center px-2 py-3 border border-white/40 text-white font-bold uppercase tracking-widest text-[9px] sm:text-[10px] hover:border-kim-red hover:text-kim-red transition-colors whitespace-nowrap">Fiche Technique</a>
        </div>
    </div>"""
content = content.replace(mobile_buttons_old, mobile_text_buttons_new)

# 3. Table styling
content = content.replace('<div class="overflow-hidden rounded-3xl border border-gray-800">', '<div class="overflow-x-auto rounded-3xl border border-gray-800">')
content = content.replace('<table class="w-full text-sm">', '<table class="w-full text-[10px] md:text-sm">')
content = content.replace('py-4 px-6', 'py-3 px-3 md:py-4 md:px-6')
content = content.replace('py-3 px-6', 'py-2 px-3 md:py-3 md:px-6')

# 4. Spacing for Motorisation
# <section class="bg-black py-24"> -> <section class="bg-black py-12 lg:py-24">
# <div class="container mx-auto px-4 lg:px-8 grid grid-cols-1 lg:grid-cols-2 gap-16 items-center"> -> gap-8 lg:gap-16
# <div class="space-y-10"> -> <div class="space-y-6 lg:space-y-10">
content = content.replace('<section class="bg-black py-24">', '<section class="bg-black py-12 lg:py-24">')
content = content.replace('gap-16 items-center', 'gap-8 lg:gap-16 items-center')
content = content.replace('<div class="space-y-10">', '<div class="space-y-6 lg:space-y-10">')

# 5. Bottom Buttons
# <a href="../media/pista-hr/fiche-technique.webp" download="Fiche-Technique-Pista-HR.webp" class="flex items-center justify-center gap-4 w-full py-5 bg-kim-red text-white font-bold uppercase tracking-widest text-sm rounded-2xl hover:bg-red-800 transition-colors group">
btn1_old = 'gap-4 w-full py-5 bg-kim-red text-white font-bold uppercase tracking-widest text-sm rounded-2xl'
btn1_new = 'gap-2 md:gap-4 w-full py-3 md:py-5 bg-kim-red text-white font-bold uppercase tracking-widest text-[9px] md:text-sm rounded-2xl whitespace-nowrap'
content = content.replace(btn1_old, btn1_new)

btn2_old = 'gap-4 w-full py-5 border border-kim-red text-kim-red font-bold uppercase tracking-widest text-sm rounded-2xl'
btn2_new = 'gap-2 md:gap-4 w-full py-3 md:py-5 border border-kim-red text-kim-red font-bold uppercase tracking-widest text-[9px] md:text-sm rounded-2xl whitespace-nowrap'
content = content.replace(btn2_old, btn2_new)

with open('modeles/pista-hr.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done pista-hr.html")
