import re

with open('modeles/ghost-v7.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1 & 2 & 3: Color picker duplicate and JS updates
old_color_selector = '''                    <!-- Color Selector -->
                    <div class="mb-10 p-6 glass-card rounded-2xl inline-block">
                        <p class="text-white/60 text-xs uppercase tracking-widest mb-4 font-bold">Sélectionnez la finition</p>
                        <div class="flex gap-4 flex-wrap">
                            <button onclick="changeColor('noir','../media/ghost-v7/kim3_GHOST-AFFICHE-NOIR-NOIR.webp')" class="ghost-color-btn w-12 h-12 rounded-full border-2 border-white ring-2 ring-white ring-offset-4 ring-offset-[#1a1a24] transition-all relative overflow-hidden" style="background:#111" title="Noir Intégral"></button>
                            <button onclick="changeColor('bleu','../media/ghost-v7/kim3_GHOST-BLEU.webp')" class="ghost-color-btn w-12 h-12 rounded-full border-2 border-transparent hover:border-white transition-all relative overflow-hidden" style="background:#2563eb" title="Bleu Électrique"></button>
                            <button onclick="changeColor('carbon','../media/ghost-v7/kim3_GHOST-CARBON.webp')" class="ghost-color-btn w-12 h-12 rounded-full border-2 border-transparent hover:border-white transition-all relative overflow-hidden" style="background:linear-gradient(45deg, #222, #444)" title="Finition Carbon"></button>
                            <button onclick="changeColor('blanc','../media/ghost-v7/kim3_GHOST-blanc.webp')" class="ghost-color-btn w-12 h-12 rounded-full border-2 border-transparent hover:border-white transition-all relative overflow-hidden" style="background:#f1f5f9" title="Blanc Pur"></button>
                            <button onclick="changeColor('vert','../media/ghost-v7/kim3_ghost-v7-vert.webp')" class="ghost-color-btn w-12 h-12 rounded-full border-2 border-transparent hover:border-white transition-all relative overflow-hidden" style="background:#16a34a" title="Vert Sport"></button>
                            <button onclick="changeColor('rouge','../media/ghost-v7/kim2_ghost-rouge-affiche.webp')" class="ghost-color-btn w-12 h-12 rounded-full border-2 border-transparent hover:border-white transition-all relative overflow-hidden" style="background:#dc2626" title="Rouge Racing"></button>
                        </div>
                        <p id="color-label" class="text-white text-sm font-bold mt-4 tracking-widest uppercase">Noir Intégral</p>
                    </div>'''

new_color_selector_desktop = '''                    <!-- Color Selector (Desktop) -->
                    <div class="mb-10 p-6 glass-card rounded-2xl hidden lg:inline-block">
                        <p class="text-white/60 text-xs uppercase tracking-widest mb-4 font-bold">Sélectionnez la couleur</p>
                        <div class="flex gap-4 flex-wrap">
                            <button data-color="noir" onclick="changeColor('noir','../media/ghost-v7/kim3_GHOST-AFFICHE-NOIR-NOIR.webp')" class="ghost-color-btn w-12 h-12 rounded-full border-2 border-white transition-all relative overflow-hidden shadow-[0_0_0_2px_#1a1a24,0_0_0_4px_#fff]" style="background:#111" title="Noir Intégral"></button>
                            <button data-color="bleu" onclick="changeColor('bleu','../media/ghost-v7/kim3_GHOST-BLEU.webp')" class="ghost-color-btn w-12 h-12 rounded-full border-2 border-transparent transition-all relative overflow-hidden" style="background:#2563eb" title="Bleu Électrique"></button>
                            <button data-color="carbon" onclick="changeColor('carbon','../media/ghost-v7/kim3_GHOST-CARBON.webp')" class="ghost-color-btn w-12 h-12 rounded-full border-2 border-transparent transition-all relative overflow-hidden" style="background:linear-gradient(45deg, #222, #444)" title="Finition Carbon"></button>
                            <button data-color="blanc" onclick="changeColor('blanc','../media/ghost-v7/kim3_GHOST-blanc.webp')" class="ghost-color-btn w-12 h-12 rounded-full border-2 border-transparent transition-all relative overflow-hidden" style="background:#f1f5f9" title="Blanc Pur"></button>
                            <button data-color="vert" onclick="changeColor('vert','../media/ghost-v7/kim3_ghost-v7-vert.webp')" class="ghost-color-btn w-12 h-12 rounded-full border-2 border-transparent transition-all relative overflow-hidden" style="background:#16a34a" title="Vert Sport"></button>
                            <button data-color="rouge" onclick="changeColor('rouge','../media/ghost-v7/kim2_ghost-rouge-affiche.webp')" class="ghost-color-btn w-12 h-12 rounded-full border-2 border-transparent transition-all relative overflow-hidden" style="background:#dc2626" title="Rouge Racing"></button>
                        </div>
                        <p class="color-label-text text-white text-sm font-bold mt-4 tracking-widest uppercase">Noir Intégral</p>
                    </div>'''

content = content.replace(old_color_selector, new_color_selector_desktop)


old_image_section = '''                <div class="order-1 lg:order-2 relative flex justify-center items-center">
                    <div class="absolute inset-0 bg-white/5 blur-[150px] rounded-full scale-90 ghost-glow"></div>
                    <img id="ghost-main-img" src="../media/ghost-v7/kim3_GHOST-AFFICHE-NOIR-NOIR.webp" alt="GHOST V7" class="relative z-10 w-full max-w-[800px] object-contain drop-shadow-2xl transition-all duration-700 hover:scale-105">
                </div>'''

new_image_section = '''                <div class="order-1 lg:order-2 relative flex flex-col justify-center items-center">
                    <div class="absolute inset-0 bg-white/5 blur-[150px] rounded-full scale-90 ghost-glow"></div>
                    <img id="ghost-main-img" src="../media/ghost-v7/kim3_GHOST-AFFICHE-NOIR-NOIR.webp" alt="GHOST V7" class="relative z-10 w-full max-w-[800px] object-contain drop-shadow-2xl transition-all duration-700 hover:scale-105 mb-6 lg:mb-0">
                    
                    <!-- Color Selector (Mobile) -->
                    <div class="p-4 glass-card rounded-2xl lg:hidden flex flex-col items-center z-20 w-full max-w-sm">
                        <p class="text-white/60 text-[10px] uppercase tracking-widest mb-3 font-bold">Sélectionnez la couleur</p>
                        <div class="flex gap-2 flex-wrap justify-center">
                            <button data-color="noir" onclick="changeColor('noir','../media/ghost-v7/kim3_GHOST-AFFICHE-NOIR-NOIR.webp')" class="ghost-color-btn w-8 h-8 rounded-full border border-white transition-all relative overflow-hidden shadow-[0_0_0_2px_#1a1a24,0_0_0_3px_#fff]" style="background:#111" title="Noir Intégral"></button>
                            <button data-color="bleu" onclick="changeColor('bleu','../media/ghost-v7/kim3_GHOST-BLEU.webp')" class="ghost-color-btn w-8 h-8 rounded-full border border-transparent transition-all relative overflow-hidden" style="background:#2563eb" title="Bleu Électrique"></button>
                            <button data-color="carbon" onclick="changeColor('carbon','../media/ghost-v7/kim3_GHOST-CARBON.webp')" class="ghost-color-btn w-8 h-8 rounded-full border border-transparent transition-all relative overflow-hidden" style="background:linear-gradient(45deg, #222, #444)" title="Finition Carbon"></button>
                            <button data-color="blanc" onclick="changeColor('blanc','../media/ghost-v7/kim3_GHOST-blanc.webp')" class="ghost-color-btn w-8 h-8 rounded-full border border-transparent transition-all relative overflow-hidden" style="background:#f1f5f9" title="Blanc Pur"></button>
                            <button data-color="vert" onclick="changeColor('vert','../media/ghost-v7/kim3_ghost-v7-vert.webp')" class="ghost-color-btn w-8 h-8 rounded-full border border-transparent transition-all relative overflow-hidden" style="background:#16a34a" title="Vert Sport"></button>
                            <button data-color="rouge" onclick="changeColor('rouge','../media/ghost-v7/kim2_ghost-rouge-affiche.webp')" class="ghost-color-btn w-8 h-8 rounded-full border border-transparent transition-all relative overflow-hidden" style="background:#dc2626" title="Rouge Racing"></button>
                        </div>
                        <p class="color-label-text text-white text-[10px] font-bold mt-3 tracking-widest uppercase">Noir Intégral</p>
                    </div>
                </div>'''
content = content.replace(old_image_section, new_image_section)

# Update JS changeColor in ghost-v7
old_js = '''    function changeColor(name, imgSrc) {
        document.getElementById('ghost-main-img').src = imgSrc;
        const labels = {
            'noir':'Noir Intégral','bleu':'Bleu Électrique','carbon':'Finition Carbon',
            'blanc':'Blanc Pur','vert':'Vert Sport','rouge':'Rouge Racing'
        };
        document.getElementById('color-label').textContent = labels[name] || name;
        
        // Update rings
        document.querySelectorAll('.ghost-color-btn').forEach(b => {
            b.classList.remove('border-white', 'ring-2', 'ring-white', 'ring-offset-4', 'ring-offset-[#1a1a24]');
            b.classList.add('border-transparent');
        });
        
        const clicked = event.currentTarget;
        clicked.classList.remove('border-transparent');
        clicked.classList.add('border-white', 'ring-2', 'ring-white', 'ring-offset-4', 'ring-offset-[#1a1a24]');
    }'''

new_js = '''    function changeColor(name, imgSrc) {
        document.getElementById('ghost-main-img').src = imgSrc;
        const labels = {
            'noir':'Noir Intégral','bleu':'Bleu Électrique','carbon':'Finition Carbon',
            'blanc':'Blanc Pur','vert':'Vert Sport','rouge':'Rouge Racing'
        };
        document.querySelectorAll('.color-label-text').forEach(el => el.textContent = labels[name] || name);
        
        // Update all buttons globally
        document.querySelectorAll('.ghost-color-btn').forEach(b => {
            b.style.borderColor = 'transparent';
            b.style.boxShadow = 'none';
        });
        
        document.querySelectorAll('.ghost-color-btn[data-color="'+name+'"]').forEach(b => {
            b.style.borderColor = 'white';
            const offsetWidth = window.innerWidth < 1024 ? '3px' : '4px';
            b.style.boxShadow = `0 0 0 2px #1a1a24, 0 0 0 ${offsetWidth} #fff`;
        });
    }'''
content = content.replace(old_js, new_js)


# 4. Marquee Height reduction
content = content.replace('<div class="marquee-track py-8">', '<div class="marquee-track py-0 md:py-2">')
content = content.replace('<div class="marquee-item"><span class="text-white/20 text-2xl">|</span></div>', '<span class="text-white/20 text-2xl px-4 md:px-6 flex items-center shrink-0">|</span>')


# 5. Margin between marquee and next section
content = content.replace('<section class="bg-black py-24 relative overflow-hidden">', '<section class="bg-black pt-12 pb-24 lg:pt-24 lg:pb-24 relative overflow-hidden">')
content = content.replace('<div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">', '<div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-16 items-center">')

# 6. Space between "Prêt à rouler" and images
content = content.replace('<section class="relative h-[80vh] w-full overflow-hidden flex items-center justify-center">', '<section class="relative min-h-[50vh] lg:min-h-0 lg:h-[80vh] w-full overflow-hidden flex items-center justify-center py-16">')
content = content.replace('<section id="specs" class="bg-black py-24 relative border-t border-white/5">', '<section id="specs" class="bg-black py-12 lg:py-24 relative border-t border-white/5">')


with open('modeles/ghost-v7.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done ghost-v7.html updates")
