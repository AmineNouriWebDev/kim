import re

with open('modeles/pista-hr-plus.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hide desktop color picker on mobile
old_color_picker = '''            <!-- Color Selector -->
            <div class="mb-10">
                <p class="text-gray-500 text-xs uppercase tracking-widest mb-4">Choisissez votre couleur</p>
                <div class="flex gap-3 flex-wrap">
                    <button onclick="changeColor('rouge','../media/pista-hr-plus/kim3_HRplus-NV-rouge.webp','#cc2200')" class="color-btn w-10 h-10 rounded-full border-2 border-kim-red ring-2 ring-kim-red ring-offset-2 ring-offset-black transition-all" style="background:#cc2200" title="Rouge"></button>
                    <button onclick="changeColor('bleu','../media/pista-hr-plus/kim3_HRplus-NV-2026-Bleu-metallise.webp','#2563eb')" class="color-btn w-10 h-10 rounded-full border-2 border-transparent hover:border-blue-500 transition-all" style="background:#2563eb" title="Bleu Métallisé"></button>
                    <button onclick="changeColor('vert','../media/pista-hr-plus/kim3_HRplus-NV-2026-vert.webp','#16a34a')" class="color-btn w-10 h-10 rounded-full border-2 border-transparent hover:border-green-500 transition-all" style="background:#16a34a" title="Vert"></button>
                    <button onclick="changeColor('noir-rouge','../media/pista-hr-plus/kim3_HRplus-NV-2026-noir-rouge.webp','#dc2626')" class="color-btn w-10 h-10 rounded-full border-2 border-transparent hover:border-red-500 transition-all" style="background:linear-gradient(135deg,#111 50%,#dc2626 50%)" title="Noir/Rouge"></button>
                    <button onclick="changeColor('carbon','../media/pista-hr-plus/kim3_HRplus-NV-2026-noir-carbon.webp','#555')" class="color-btn w-10 h-10 rounded-full border-2 border-transparent hover:border-gray-400 transition-all" style="background:#222" title="Noir Carbon"></button>
                </div>
                <p id="color-label" class="text-kim-red text-sm font-bold mt-3 tracking-widest uppercase">Rouge</p>
            </div>'''

new_color_picker_desktop = '''            <!-- Color Selector (Desktop) -->
            <div class="mb-10 hidden lg:block">
                <p class="text-gray-500 text-xs uppercase tracking-widest mb-4">Choisissez votre couleur</p>
                <div class="flex gap-3 flex-wrap">
                    <button data-color="rouge" onclick="changeColor('rouge','../media/pista-hr-plus/kim3_HRplus-NV-rouge.webp','#cc2200')" class="color-btn w-10 h-10 rounded-full border-2 border-kim-red ring-2 ring-kim-red ring-offset-2 ring-offset-black transition-all" style="background:#cc2200" title="Rouge"></button>
                    <button data-color="bleu" onclick="changeColor('bleu','../media/pista-hr-plus/kim3_HRplus-NV-2026-Bleu-metallise.webp','#2563eb')" class="color-btn w-10 h-10 rounded-full border-2 border-transparent hover:border-blue-500 transition-all" style="background:#2563eb" title="Bleu Métallisé"></button>
                    <button data-color="vert" onclick="changeColor('vert','../media/pista-hr-plus/kim3_HRplus-NV-2026-vert.webp','#16a34a')" class="color-btn w-10 h-10 rounded-full border-2 border-transparent hover:border-green-500 transition-all" style="background:#16a34a" title="Vert"></button>
                    <button data-color="noir-rouge" onclick="changeColor('noir-rouge','../media/pista-hr-plus/kim3_HRplus-NV-2026-noir-rouge.webp','#dc2626')" class="color-btn w-10 h-10 rounded-full border-2 border-transparent hover:border-red-500 transition-all" style="background:linear-gradient(135deg,#111 50%,#dc2626 50%)" title="Noir/Rouge"></button>
                    <button data-color="carbon" onclick="changeColor('carbon','../media/pista-hr-plus/kim3_HRplus-NV-2026-noir-carbon.webp','#555')" class="color-btn w-10 h-10 rounded-full border-2 border-transparent hover:border-gray-400 transition-all" style="background:#222" title="Noir Carbon"></button>
                </div>
                <p class="color-label-text text-kim-red text-sm font-bold mt-3 tracking-widest uppercase">Rouge</p>
            </div>'''
content = content.replace(old_color_picker, new_color_picker_desktop)

# 2. Add mobile color picker under the image
image_section = '''        <!-- Right: Bike image (interactive) -->
        <div class="w-full lg:w-1/2 relative flex items-center justify-center min-h-[60vw] lg:min-h-0">
            <div id="color-glow" class="absolute inset-0 blur-[120px] opacity-30 transition-all duration-700" style="background:#cc2200"></div>
            <img id="color-image" src="../media/pista-hr-plus/kim3_HRplus-NV-rouge.webp" alt="PISTA HR+" class="relative z-10 w-full max-w-2xl object-contain transition-all duration-500 drop-shadow-2xl px-4">
        </div>
    </section>'''

new_image_section = '''        <!-- Right: Bike image (interactive) -->
        <div class="w-full lg:w-1/2 relative flex flex-col items-center justify-center min-h-[60vw] lg:min-h-0">
            <div class="relative w-full flex items-center justify-center pb-8 lg:pb-0">
                <div id="color-glow" class="absolute inset-0 blur-[120px] opacity-30 transition-all duration-700" style="background:#cc2200"></div>
                <img id="color-image" src="../media/pista-hr-plus/kim3_HRplus-NV-rouge.webp" alt="PISTA HR+" class="relative z-10 w-full max-w-2xl object-contain transition-all duration-500 drop-shadow-2xl px-4 mt-8 lg:mt-0">
            </div>
            
            <!-- Color Selector (Mobile) -->
            <div class="lg:hidden w-full px-8 pb-10 flex flex-col items-center z-20">
                <p class="text-gray-500 text-[10px] uppercase tracking-widest mb-4">Choisissez votre couleur</p>
                <div class="flex gap-2 flex-wrap justify-center">
                    <button data-color="rouge" onclick="changeColor('rouge','../media/pista-hr-plus/kim3_HRplus-NV-rouge.webp','#cc2200')" class="color-btn w-8 h-8 md:w-10 md:h-10 rounded-full border-2 border-kim-red ring-2 ring-kim-red ring-offset-2 ring-offset-black transition-all" style="background:#cc2200" title="Rouge"></button>
                    <button data-color="bleu" onclick="changeColor('bleu','../media/pista-hr-plus/kim3_HRplus-NV-2026-Bleu-metallise.webp','#2563eb')" class="color-btn w-8 h-8 md:w-10 md:h-10 rounded-full border-2 border-transparent hover:border-blue-500 transition-all" style="background:#2563eb" title="Bleu Métallisé"></button>
                    <button data-color="vert" onclick="changeColor('vert','../media/pista-hr-plus/kim3_HRplus-NV-2026-vert.webp','#16a34a')" class="color-btn w-8 h-8 md:w-10 md:h-10 rounded-full border-2 border-transparent hover:border-green-500 transition-all" style="background:#16a34a" title="Vert"></button>
                    <button data-color="noir-rouge" onclick="changeColor('noir-rouge','../media/pista-hr-plus/kim3_HRplus-NV-2026-noir-rouge.webp','#dc2626')" class="color-btn w-8 h-8 md:w-10 md:h-10 rounded-full border-2 border-transparent hover:border-red-500 transition-all" style="background:linear-gradient(135deg,#111 50%,#dc2626 50%)" title="Noir/Rouge"></button>
                    <button data-color="carbon" onclick="changeColor('carbon','../media/pista-hr-plus/kim3_HRplus-NV-2026-noir-carbon.webp','#555')" class="color-btn w-8 h-8 md:w-10 md:h-10 rounded-full border-2 border-transparent hover:border-gray-400 transition-all" style="background:#222" title="Noir Carbon"></button>
                </div>
                <p class="color-label-text text-kim-red text-[10px] md:text-sm font-bold mt-4 tracking-widest uppercase">Rouge</p>
            </div>
        </div>
    </section>'''
content = content.replace(image_section, new_image_section)

# 3. Update changeColor function
old_js = '''    function changeColor(name, imgSrc, glowColor) {
        document.getElementById('color-image').src = imgSrc;
        document.getElementById('color-glow').style.background = glowColor;
        const labels = {
            'rouge':'Rouge','bleu':'Bleu Métallisé','vert':'Vert','noir-rouge':'Noir / Rouge','carbon':'Noir Carbon'
        };
        document.getElementById('color-label').textContent = labels[name] || name;
        document.querySelectorAll('.color-btn').forEach(b => b.style.borderColor = 'transparent');
        event.currentTarget.style.borderColor = glowColor;
    }'''
new_js = '''    function changeColor(name, imgSrc, glowColor) {
        document.getElementById('color-image').src = imgSrc;
        document.getElementById('color-glow').style.background = glowColor;
        const labels = {
            'rouge':'Rouge','bleu':'Bleu Métallisé','vert':'Vert','noir-rouge':'Noir / Rouge','carbon':'Noir Carbon'
        };
        document.querySelectorAll('.color-label-text').forEach(el => el.textContent = labels[name] || name);
        document.querySelectorAll('.color-btn').forEach(b => b.style.borderColor = 'transparent');
        // Update both mobile and desktop buttons
        document.querySelectorAll('.color-btn[data-color="'+name+'"]').forEach(b => b.style.borderColor = glowColor);
    }'''
content = content.replace(old_js, new_js)

with open('modeles/pista-hr-plus.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done pista-hr-plus.html layout update")
