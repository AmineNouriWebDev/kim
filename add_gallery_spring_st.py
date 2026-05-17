import re

with open('modeles/power-spring-st.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_gallery_sections = '''    <!-- ===== SECTION: GALERIE ===== -->
    <section class="bg-kim-darker py-12 lg:py-24 relative border-t border-gray-900">
        <div class="container mx-auto px-4 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div class="rounded-3xl overflow-hidden shadow-2xl border border-white/5">
                    <img src="../media/power-spring-st/kim3_4.webp" alt="Détail Power Spring ST" class="w-full h-64 md:h-80 object-cover hover:scale-110 transition-transform duration-700">
                </div>
                <div class="rounded-3xl overflow-hidden shadow-2xl border border-white/5">
                    <img src="../media/power-spring-st/kim3_032.webp" alt="Détail Power Spring ST" class="w-full h-64 md:h-80 object-cover hover:scale-110 transition-transform duration-700">
                </div>
                <div class="rounded-3xl overflow-hidden shadow-2xl border border-white/5">
                    <img src="../media/power-spring-st/kim3_AMIR-MOTO-Timeline-1-Resolve.00_00_23_09.Still001-copie.webp" alt="Détail Power Spring ST" class="w-full h-64 md:h-80 object-cover hover:scale-110 transition-transform duration-700">
                </div>
            </div>
        </div>
    </section>

    <!-- ===== SECTION: FULL WIDTH IMAGE ===== -->
    <section class="w-full relative overflow-hidden">
        <img src="../media/power-spring-st/kim3_spot-moto-Final25.webp" alt="Power Spring ST en action" class="w-full h-[40vh] md:h-[60vh] lg:h-[80vh] object-cover">
    </section>

    <!-- ===== SECTION 5: FICHE TECHNIQUE ===== -->'''

content = content.replace('    <!-- ===== SECTION 5: FICHE TECHNIQUE ===== -->', new_gallery_sections)

with open('modeles/power-spring-st.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done adding gallery to power-spring-st.html")
