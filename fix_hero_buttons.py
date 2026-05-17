import os
import glob

files = glob.glob('modeles/*.html')
for filepath in files:
    if filepath == 'modeles/pista-hr.html':
        continue # Already done
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find the buttons in hero section.
    # Usually it's `<div class="flex flex-wrap gap-4">` followed by `<a href="../devis.html"...`
    old_btn_container = '<div class="flex flex-wrap gap-4">\n                <a href="../devis.html"'
    new_btn_container = '<div class="hidden md:flex flex-wrap gap-4">\n                <a href="../devis.html"'
    
    if old_btn_container in content:
        content = content.replace(old_btn_container, new_btn_container)
    elif '<div class="flex flex-wrap gap-4">' in content and '../devis.html' in content:
        # fallback
        import re
        content = re.sub(r'<div class="flex flex-wrap gap-4">(\s*<a href="\.\./devis\.html")', r'<div class="hidden md:flex flex-wrap gap-4">\1', content)
        
    # Now find the end of the hero section
    # The hero section ends with </section> followed by an empty line or <!-- ===== SECTION 1
    # Actually, all model pages have "<!-- ===== SECTION 1" or similar right after the first </section>
    # The first </section> in the file is the hero section.
    
    # Or find <!-- Key stats bar --> ... </section>
    hero_end_idx = content.find('</section>')
    if hero_end_idx != -1:
        insertion_point = hero_end_idx + len('</section>')
        
        mobile_buttons = """

    <!-- ===== MOBILE BUTTONS (Under Video) ===== -->
    <div class="md:hidden flex justify-center gap-3 py-6 px-4 bg-black border-b border-gray-900">
        <a href="../devis.html" class="flex-1 text-center px-2 py-3 bg-kim-red text-white font-bold uppercase tracking-widest text-[10px] hover:bg-red-800 transition-colors">Demander un Devis</a>
        <a href="#fiche" class="flex-1 text-center px-2 py-3 border border-white/40 text-white font-bold uppercase tracking-widest text-[10px] hover:border-kim-red hover:text-kim-red transition-colors">Fiche Technique</a>
    </div>"""
        
        if "<!-- ===== MOBILE BUTTONS (Under Video) ===== -->" not in content:
            content = content[:insertion_point] + mobile_buttons + content[insertion_point:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"Could not find </section> in {filepath}")

