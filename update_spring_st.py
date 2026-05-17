import re

with open('modeles/power-spring-st.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove kim3_affiche-spring.webp
old_affiche_block = '''            <div class="mt-20">
                <img src="../media/power-spring-st/kim3_affiche-spring.webp" alt="Power Spring ST Tech" class="w-full rounded-3xl object-cover shadow-2xl">
            </div>'''
content = content.replace(old_affiche_block, '')

# 2. Restore kim3.mp4
old_image_block = '''<div class="relative w-full aspect-square rounded-[30px] overflow-hidden shadow-2xl border border-white/10">
                        <img src="../media/power-spring-st/kim3_1.webp" alt="Power Spring ST Confort" class="w-full h-full object-cover">
                    </div>'''
new_video_block = '''<div class="relative w-full aspect-square rounded-[30px] overflow-hidden shadow-2xl border border-white/10">
                        <video autoplay loop muted playsinline class="w-full h-full object-cover">
                            <source src="../media/power-spring-st/kim3.mp4" type="video/mp4">
                        </video>
                    </div>'''
content = content.replace(old_image_block, new_video_block)

# 3. Compact Dimensions Table
old_dimensions_table = '''                        <!-- Dimensions -->
                        <div>
                            <div class="bg-[#111] py-4 px-6 flex items-center gap-4">
                                <i class="fa-solid fa-ruler-combined text-kim-gold text-xl"></i>
                                <h3 class="font-sport text-2xl font-bold text-white tracking-wide m-0">DIMENSIONS & POIDS</h3>
                            </div>
                            <div class="p-6 grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-4">
                                <div><p class="text-gray-500 text-xs uppercase tracking-wider mb-1">Longueur</p><p class="text-gray-200 font-medium">1.860 mm</p></div>
                                <div><p class="text-gray-500 text-xs uppercase tracking-wider mb-1">Largeur</p><p class="text-gray-200 font-medium">740 mm</p></div>
                                <div><p class="text-gray-500 text-xs uppercase tracking-wider mb-1">Hauteur</p><p class="text-gray-200 font-medium">1.150 mm</p></div>
                                <div><p class="text-gray-500 text-xs uppercase tracking-wider mb-1">Empattement</p><p class="text-gray-200 font-medium">1.300 mm</p></div>
                                <div><p class="text-gray-500 text-xs uppercase tracking-wider mb-1">Poids</p><p class="text-gray-200 font-medium">251 kg</p></div>
                            </div>
                        </div>'''

new_dimensions_table = '''                        <!-- Dimensions -->
                        <div>
                            <div class="bg-[#111] py-4 px-6 flex items-center gap-4">
                                <i class="fa-solid fa-ruler-combined text-kim-gold text-xl"></i>
                                <h3 class="font-sport text-2xl font-bold text-white tracking-wide m-0">DIMENSIONS & POIDS</h3>
                            </div>
                            <div class="p-6 grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-4">
                                <div class="flex justify-between items-center border-b border-white/10 pb-2"><span class="text-gray-500 text-xs uppercase tracking-wider">Longueur</span><span class="text-gray-200 font-medium text-right">1.860 mm</span></div>
                                <div class="flex justify-between items-center border-b border-white/10 pb-2"><span class="text-gray-500 text-xs uppercase tracking-wider">Largeur</span><span class="text-gray-200 font-medium text-right">740 mm</span></div>
                                <div class="flex justify-between items-center border-b border-white/10 pb-2"><span class="text-gray-500 text-xs uppercase tracking-wider">Hauteur</span><span class="text-gray-200 font-medium text-right">1.150 mm</span></div>
                                <div class="flex justify-between items-center border-b border-white/10 pb-2"><span class="text-gray-500 text-xs uppercase tracking-wider">Empattement</span><span class="text-gray-200 font-medium text-right">1.300 mm</span></div>
                                <div class="flex justify-between items-center border-b border-white/10 pb-2 md:col-span-2"><span class="text-gray-500 text-xs uppercase tracking-wider">Poids</span><span class="text-gray-200 font-medium text-right">251 kg</span></div>
                            </div>
                        </div>'''

content = content.replace(old_dimensions_table, new_dimensions_table)

with open('modeles/power-spring-st.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done updating power-spring-st.html")
