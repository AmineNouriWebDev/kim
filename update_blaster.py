import re

with open('modeles/blaster.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1 & 4. Marquee: add overflow-hidden, reduce padding, fix separators
content = content.replace('<section class="bg-kim-efi py-0 border-y border-sky-400 shadow-[0_0_30px_rgba(14,165,233,0.2)] relative z-20">', '<section class="bg-kim-efi py-0 border-y border-sky-400 shadow-[0_0_30px_rgba(14,165,233,0.2)] relative z-20 overflow-hidden">')
content = content.replace('<div class="marquee-track py-5">', '<div class="marquee-track py-0 md:py-2">')
content = content.replace('<div class="marquee-item"><span class="text-white/30 text-2xl">•</span></div>', '<span class="text-white/30 text-2xl px-4 md:px-6 flex items-center shrink-0">•</span>')


# 2 & 3. Remove button, duplicate color picker, and update JS
old_color_selector = '''                    <!-- Color Selector -->
                    <div class="mb-10 p-5 bg-black/40 border border-white/5 rounded-2xl inline-block backdrop-blur-md">
                        <p class="text-white/40 text-xs uppercase tracking-widest mb-4 font-bold">Variantes Disponibles</p>
                        <div class="flex gap-4 flex-wrap">
                            <button onclick="changeColor('noir','../media/blaster/kim3_blaster-noir-copie.webp')" class="color-btn w-10 h-10 rounded-full border-2 border-white ring-2 ring-white ring-offset-2 ring-offset-black transition-all" style="background:#1a1a1a" title="Noir"></button>
                            <button onclick="changeColor('rouge','../media/blaster/kim3_blaster-rouge--copie.webp')" class="color-btn w-10 h-10 rounded-full border-2 border-transparent hover:border-white transition-all" style="background:#dc2626" title="Rouge"></button>
                            <button onclick="changeColor('bleu-cyan','../media/blaster/kim3_blaster-vert-claire.webp')" class="color-btn w-10 h-10 rounded-full border-2 border-transparent hover:border-white transition-all" style="background:#B4FAFC" title="Bleu Cyan"></button>
                            <button onclick="changeColor('vert','../media/blaster/kim3_vert--copie.webp')" class="color-btn w-10 h-10 rounded-full border-2 border-transparent hover:border-white transition-all" style="background:#15803d" title="Vert"></button>
                        </div>
                    </div>
                    
                    <div class="hidden md:flex flex-wrap gap-4">
                        <a href="../devis.html" class="px-10 py-4 bg-kim-efi text-white font-bold uppercase tracking-widest text-sm hover:bg-sky-600 transition-colors shadow-[0_0_20px_rgba(14,165,233,0.3)] hover:shadow-[0_0_30px_rgba(14,165,233,0.5)]">Passer à l'injection</a>
                    </div>'''

new_color_selector_desktop = '''                    <!-- Color Selector (Desktop) -->
                    <div class="mb-10 p-5 bg-black/40 border border-white/5 rounded-2xl hidden lg:inline-block backdrop-blur-md">
                        <p class="text-white/40 text-xs uppercase tracking-widest mb-4 font-bold">Variantes Disponibles</p>
                        <div class="flex gap-4 flex-wrap">
                            <button data-color="noir" onclick="changeColor('noir','../media/blaster/kim3_blaster-noir-copie.webp')" class="color-btn w-10 h-10 rounded-full transition-all" style="background:#1a1a1a; border-color: white; box-shadow: 0 0 0 2px #0a0a0c, 0 0 0 4px white;" title="Noir"></button>
                            <button data-color="rouge" onclick="changeColor('rouge','../media/blaster/kim3_blaster-rouge--copie.webp')" class="color-btn w-10 h-10 rounded-full transition-all border border-transparent" style="background:#dc2626" title="Rouge"></button>
                            <button data-color="bleu-cyan" onclick="changeColor('bleu-cyan','../media/blaster/kim3_blaster-vert-claire.webp')" class="color-btn w-10 h-10 rounded-full transition-all border border-transparent" style="background:#B4FAFC" title="Bleu Cyan"></button>
                            <button data-color="vert" onclick="changeColor('vert','../media/blaster/kim3_vert--copie.webp')" class="color-btn w-10 h-10 rounded-full transition-all border border-transparent" style="background:#15803d" title="Vert"></button>
                        </div>
                    </div>'''
content = content.replace(old_color_selector, new_color_selector_desktop)

old_image_container = '''                <div class="order-1 lg:order-2 relative flex justify-center items-center">
                    <!-- Tech circles -->
                    <div class="absolute inset-0 flex items-center justify-center pointer-events-none">
                        <div class="w-[400px] h-[400px] border border-white/5 rounded-full absolute"></div>
                        <div class="w-[600px] h-[600px] border border-kim-efi/10 rounded-full absolute"></div>
                    </div>
                    <img id="blaster-main-img" src="../media/blaster/kim3_blaster-noir-copie.webp" alt="BLASTER" class="relative z-10 w-full max-w-[800px] object-contain drop-shadow-[0_20px_50px_rgba(0,0,0,0.5)] transition-all duration-700 hover:scale-105">
                </div>'''

new_image_container = '''                <div class="order-1 lg:order-2 relative flex flex-col justify-center items-center">
                    <!-- Tech circles -->
                    <div class="absolute inset-0 flex items-center justify-center pointer-events-none">
                        <div class="w-[400px] h-[400px] border border-white/5 rounded-full absolute"></div>
                        <div class="w-[600px] h-[600px] border border-kim-efi/10 rounded-full absolute"></div>
                    </div>
                    <img id="blaster-main-img" src="../media/blaster/kim3_blaster-noir-copie.webp" alt="BLASTER" class="relative z-10 w-full max-w-[800px] object-contain drop-shadow-[0_20px_50px_rgba(0,0,0,0.5)] transition-all duration-700 hover:scale-105 mb-6 lg:mb-0">
                    
                    <!-- Color Selector (Mobile) -->
                    <div class="p-4 bg-black/40 border border-white/5 rounded-2xl lg:hidden flex flex-col items-center z-20 w-full max-w-sm backdrop-blur-md">
                        <p class="text-white/40 text-[10px] uppercase tracking-widest mb-3 font-bold">Variantes Disponibles</p>
                        <div class="flex gap-3 flex-wrap justify-center">
                            <button data-color="noir" onclick="changeColor('noir','../media/blaster/kim3_blaster-noir-copie.webp')" class="color-btn w-8 h-8 rounded-full transition-all" style="background:#1a1a1a; border-color: white; box-shadow: 0 0 0 2px #0a0a0c, 0 0 0 3px white;" title="Noir"></button>
                            <button data-color="rouge" onclick="changeColor('rouge','../media/blaster/kim3_blaster-rouge--copie.webp')" class="color-btn w-8 h-8 rounded-full transition-all border border-transparent" style="background:#dc2626" title="Rouge"></button>
                            <button data-color="bleu-cyan" onclick="changeColor('bleu-cyan','../media/blaster/kim3_blaster-vert-claire.webp')" class="color-btn w-8 h-8 rounded-full transition-all border border-transparent" style="background:#B4FAFC" title="Bleu Cyan"></button>
                            <button data-color="vert" onclick="changeColor('vert','../media/blaster/kim3_vert--copie.webp')" class="color-btn w-8 h-8 rounded-full transition-all border border-transparent" style="background:#15803d" title="Vert"></button>
                        </div>
                    </div>
                </div>'''
content = content.replace(old_image_container, new_image_container)

old_js = '''    <script>
        function changeColor(name, imgSrc) {
            document.getElementById('blaster-main-img').src = imgSrc;
            
            document.querySelectorAll('.color-btn').forEach(b => {
                b.classList.remove('border-white', 'ring-2', 'ring-white', 'ring-offset-2', 'ring-offset-black');
                b.classList.add('border-transparent');
            });
            event.currentTarget.classList.remove('border-transparent');
            event.currentTarget.classList.add('border-white', 'ring-2', 'ring-white', 'ring-offset-2', 'ring-offset-black');
        }
    </script>'''

new_js = '''    <script>
        function changeColor(name, imgSrc) {
            document.getElementById('blaster-main-img').src = imgSrc;
            
            document.querySelectorAll('.color-btn').forEach(b => {
                b.style.borderColor = 'transparent';
                b.style.boxShadow = 'none';
            });
            
            document.querySelectorAll('.color-btn[data-color="'+name+'"]').forEach(b => {
                b.style.borderColor = 'white';
                const offsetWidth = window.innerWidth < 1024 ? '3px' : '4px';
                b.style.boxShadow = `0 0 0 2px #0a0a0c, 0 0 0 ${offsetWidth} #fff`;
            });
        }
    </script>'''
content = content.replace(old_js, new_js)

# 5. Icons in Endurance & Securite
old_card1 = '''                        <div class="bg-[#111] p-6 rounded-2xl border border-gray-800 hover:border-kim-efi transition-colors">
                            <i class="fa-solid fa-droplet text-kim-efi text-3xl mb-4"></i>
                            <h4 class="text-white font-bold text-lg mb-2">Endurance Parfaite</h4>
                            <p class="text-gray-500 text-sm">Le refroidissement liquide maintient des performances constantes là où les autres s’essoufflent.</p>
                        </div>'''
new_card1 = '''                        <div class="bg-[#111] p-6 rounded-2xl border border-gray-800 hover:border-kim-efi transition-colors">
                            <div class="flex items-center gap-4 mb-3">
                                <i class="fa-solid fa-droplet text-kim-efi text-2xl"></i>
                                <h4 class="text-white font-bold text-lg">Endurance Parfaite</h4>
                            </div>
                            <p class="text-gray-500 text-sm">Le refroidissement liquide maintient des performances constantes là où les autres s’essoufflent.</p>
                        </div>'''

old_card2 = '''                        <div class="bg-[#111] p-6 rounded-2xl border border-gray-800 hover:border-kim-efi transition-colors">
                            <i class="fa-solid fa-circle-stop text-kim-efi text-3xl mb-4"></i>
                            <h4 class="text-white font-bold text-lg mb-2">Sécurité Totale</h4>
                            <p class="text-gray-500 text-sm">Disques de frein ventilés (AV/AR) assurant un mordant progressif et puissant sur tout terrain.</p>
                        </div>'''
new_card2 = '''                        <div class="bg-[#111] p-6 rounded-2xl border border-gray-800 hover:border-kim-efi transition-colors">
                            <div class="flex items-center gap-4 mb-3">
                                <i class="fa-solid fa-circle-stop text-kim-efi text-2xl"></i>
                                <h4 class="text-white font-bold text-lg">Sécurité Totale</h4>
                            </div>
                            <p class="text-gray-500 text-sm">Disques de frein ventilés (AV/AR) assurant un mordant progressif et puissant sur tout terrain.</p>
                        </div>'''

content = content.replace(old_card1, new_card1)
content = content.replace(old_card2, new_card2)

with open('modeles/blaster.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done updating blaster.html")
