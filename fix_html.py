import os
import re

mobile_menu_template = """    <!-- Mobile Menu -->
    <div id="mobile-menu" class="fixed inset-0 z-40 bg-white/95 dark:bg-kim-darker/95 backdrop-blur-3xl transform translate-x-full transition-transform duration-500 pt-24 px-8 md:hidden flex flex-col overflow-y-auto pb-10">
        <a href="{root}index.html" class="mobile-link text-4xl font-sport font-bold tracking-widest border-b border-gray-200 dark:border-gray-800 py-6 text-kim-red">ACCUEIL</a>
        <div class="py-6 border-b border-gray-200 dark:border-gray-800">
            <span class="text-4xl font-sport font-bold tracking-widest text-gray-500 mb-4 block">MODÈLES</span>
            <div class="grid grid-cols-2 gap-4 pl-4">
                <a href="{mod}pista-hr.html" class="font-bold text-lg">PISTA HR</a>
                <a href="{mod}pista-hr-plus.html" class="font-bold text-lg">PISTA HR+</a>
                <a href="{mod}pista-vcx.html" class="font-bold text-lg">PISTA VCX</a>
                <a href="{mod}ghost-v7.html" class="font-bold text-lg">GHOST V7</a>
                <a href="{mod}black-street.html" class="font-bold text-lg">BLACK STREET</a>
                <a href="{mod}power-spring-st.html" class="font-bold text-lg">SPRING ST</a>
                <a href="{mod}blaster.html" class="font-bold text-lg text-kim-red">BLASTER</a>
            </div>
        </div>
        <a href="{root}a-propos.html" class="mobile-link text-4xl font-sport font-bold tracking-widest border-b border-gray-200 dark:border-gray-800 py-6">À PROPOS</a>
        <a href="{root}atelier.html" class="mobile-link text-4xl font-sport font-bold tracking-widest border-b border-gray-200 dark:border-gray-800 py-6">L'ATELIER</a>
        <a href="{root}contact.html" class="mobile-link text-4xl font-sport font-bold tracking-widest py-6">CONTACT</a>
        <button id="close-mobile-menu" class="absolute top-6 right-6 p-4 text-gray-800 dark:text-gray-200">
            <i class="fa-solid fa-xmark text-4xl"></i>
        </button>
    </div>"""

root_files = ['atelier.html', 'contact.html', 'devis.html', 'a-propos.html', 'index.html']
model_files = [
    'modeles/pista-hr.html', 'modeles/pista-hr-plus.html', 'modeles/pista-vcx.html',
    'modeles/ghost-v7.html', 'modeles/black-street.html', 'modeles/power-spring-st.html',
    'modeles/power-125.html', 'modeles/power-110.html', 'modeles/blaster.html'
]

for file_path in root_files + model_files:
    if not os.path.exists(file_path): continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    is_model = file_path.startswith('modeles/')
    
    # Generate correct mobile menu block
    root_pfx = '../' if is_model else ''
    mod_pfx = '' if is_model else 'modeles/'
    
    correct_mobile_menu = mobile_menu_template.format(root=root_pfx, mod=mod_pfx)
    
    # Find start of Mobile Menu
    menu_start_idx = content.find('<!-- Mobile Menu -->')
    
    if menu_start_idx != -1:
        # Find start of the main content
        main_start_idx = content.find('<main', menu_start_idx)
        if main_start_idx == -1:
            main_start_idx = content.find('<!-- Hero Section -->', menu_start_idx)
            
        if main_start_idx != -1:
            # Replace everything between menu_start and main_start
            new_content = content[:menu_start_idx] + correct_mobile_menu + '\n\n' + content[main_start_idx:]
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {file_path}")
        else:
            print(f"Could not find main start in {file_path}")
    else:
        print(f"Could not find Mobile Menu in {file_path}")

