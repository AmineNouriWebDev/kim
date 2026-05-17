import re

with open('modeles/power-spring-st.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Horizontal scroll in marquee section
content = content.replace(
    '<section class="bg-black py-0 border-y border-gray-900 relative z-20">',
    '<section class="bg-black py-0 border-y border-gray-900 relative z-20 overflow-hidden">'
)

# 2. Marquee height & speed & spacing
content = content.replace(
    '<div class="marquee-track py-6">',
    '<div class="marquee-track py-0 md:py-2" style="animation-duration: 15s;">'
)
content = content.replace(
    '<div class="marquee-item"><span class="text-gray-800 text-2xl">/</span></div>',
    '<span class="text-gray-800 text-2xl px-4 md:px-6 flex items-center shrink-0">/</span>'
)

# 3. Missing video
old_video = '''<div class="relative w-full aspect-square rounded-[30px] overflow-hidden shadow-2xl border border-white/10">
                        <video autoplay loop muted playsinline class="w-full h-full object-cover">
                            <source src="../media/power-spring-st/kim3.mp4" type="video/mp4">
                        </video>
                    </div>'''
new_image = '''<div class="relative w-full aspect-square rounded-[30px] overflow-hidden shadow-2xl border border-white/10">
                        <img src="../media/power-spring-st/kim3_1.webp" alt="Power Spring ST Confort" class="w-full h-full object-cover">
                    </div>'''
content = content.replace(old_video, new_image)

with open('modeles/power-spring-st.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done power-spring-st.html layout fixes")
