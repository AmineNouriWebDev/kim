import os
import re
import glob

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    is_root = '/' not in filepath.replace('./', '') and 'modeles/' not in filepath
    base_path = 'media/' if is_root else '../media/'
    model_path = 'modeles/' if is_root else ''

    # --- 1. Update Mega Menu ---
    # We will replace the entire grid inside mega-menu
    mega_menu_pattern = re.compile(r'(<div id="mega-menu"[^>]*>.*?<div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-8">).*?(</div>\s*</div>\s*</div>)', re.DOTALL)
    
    mega_items = f"""
                    <a href="{model_path}pista-hr.html" class="mega-menu-item block group">
                        <div class="aspect-video bg-kim-gray mb-4 overflow-hidden rounded-lg flex items-center justify-center p-4">
                            <img src="{base_path}pista-hr/kim1_hr-affiche-2.1.webp" alt="Pista HR" class="w-full h-full object-cover">
                        </div>
                        <h4 class="font-sport font-bold text-2xl tracking-wide {"text-white" if not is_root else ""} group-hover:text-kim-red transition-colors">PISTA HR</h4>
                    </a>
                    <a href="{model_path}pista-hr-plus.html" class="mega-menu-item block group">
                        <div class="aspect-video bg-kim-gray mb-4 overflow-hidden rounded-lg flex items-center justify-center p-4">
                            <img src="{base_path}pista-hr/kim1_hr-affiche-2.1.webp" alt="Pista HR+" class="w-full h-full object-cover filter hue-rotate-90">
                        </div>
                        <h4 class="font-sport font-bold text-2xl tracking-wide {"text-white" if not is_root else ""} group-hover:text-kim-red transition-colors">PISTA HR+</h4>
                    </a>
                    <a href="{model_path}pista-vcx.html" class="mega-menu-item block group">
                        <div class="aspect-video bg-kim-gray mb-4 overflow-hidden rounded-lg flex items-center justify-center p-4">
                            <img src="{base_path}pista-vcx/kim1_PISTA-1.webp" alt="Pista VCX" class="w-full h-full object-cover">
                        </div>
                        <h4 class="font-sport font-bold text-2xl tracking-wide {"text-white" if not is_root else ""} group-hover:text-kim-red transition-colors">PISTA VCX</h4>
                    </a>
                    <a href="{model_path}ghost-v7.html" class="mega-menu-item block group">
                        <div class="aspect-video bg-kim-gray mb-4 overflow-hidden rounded-lg flex items-center justify-center p-4">
                            <img src="{base_path}ghost-v7/kim2_AFF.webp" alt="Ghost V7" class="w-full h-full object-cover">
                        </div>
                        <h4 class="font-sport font-bold text-2xl tracking-wide {"text-white" if not is_root else ""} group-hover:text-kim-red transition-colors">GHOST V7</h4>
                    </a>
                    <a href="{model_path}black-street.html" class="mega-menu-item block group">
                        <div class="aspect-video bg-kim-gray mb-4 overflow-hidden rounded-lg flex items-center justify-center p-4">
                            <img src="{base_path}black-street/kim1_DSC06092.webp" alt="Black Street" class="w-full h-full object-cover">
                        </div>
                        <h4 class="font-sport font-bold text-2xl tracking-wide {"text-white" if not is_root else ""} group-hover:text-kim-red transition-colors">BLACK STREET</h4>
                    </a>
                    <a href="{model_path}power-spring-st.html" class="mega-menu-item block group">
                        <div class="aspect-video bg-kim-gray mb-4 overflow-hidden rounded-lg flex items-center justify-center p-4 relative">
                            <img src="{base_path}power-spring-st/kim3_affiche-spring.webp" alt="Power Spring ST" class="w-full h-full object-cover">
                            <div class="absolute inset-0 bg-black/40 group-hover:bg-transparent transition-colors"></div>
                        </div>
                        <h4 class="font-sport font-bold text-2xl tracking-wide {"text-white" if not is_root else ""} group-hover:text-kim-red transition-colors">POWER SPRING ST</h4>
                    </a>
                    <a href="#" class="mega-menu-item block group opacity-50 cursor-not-allowed" title="Bientôt disponible">
                        <div class="aspect-video bg-kim-gray mb-4 overflow-hidden rounded-lg flex items-center justify-center p-4 relative">
                            <div class="w-full h-full bg-gray-700"></div>
                            <div class="absolute inset-0 flex items-center justify-center bg-black/40"><span class="text-white font-sport text-xl tracking-widest">BIENTÔT</span></div>
                        </div>
                        <h4 class="font-sport font-bold text-2xl tracking-wide {"text-white" if not is_root else ""} group-hover:text-kim-red transition-colors">POWER</h4>
                    </a>
                    <a href="{model_path}blaster.html" class="mega-menu-item block group">
                        <div class="aspect-video bg-kim-gray mb-4 overflow-hidden rounded-lg flex items-center justify-center p-4 relative">
                            <img src="{base_path}blaster/kim3_affiche-blaster-copie.webp" alt="Blaster" class="w-full h-full object-cover">
                            <div class="absolute inset-0 bg-black/40 group-hover:bg-transparent transition-colors"></div>
                        </div>
                        <h4 class="font-sport font-bold text-2xl tracking-wide {"text-white" if not is_root else ""} group-hover:text-kim-red transition-colors">BLASTER</h4>
                    </a>
"""
    content = mega_menu_pattern.sub(r'\1' + mega_items + r'\2', content)

    # --- 2. Update Mobile Menu ---
    mobile_menu_pattern = re.compile(r'(<div id="mobile-menu".*?<div class="grid grid-cols-2 gap-4 pl-4">).*?(</div>\s*</div>)', re.DOTALL)
    
    # We want to keep the mobile menu simple but updated
    mobile_items = f"""
                <a href="{model_path}pista-hr.html" class="font-bold text-lg">PISTA HR</a>
                <a href="{model_path}pista-hr-plus.html" class="font-bold text-lg">PISTA HR+</a>
                <a href="{model_path}pista-vcx.html" class="font-bold text-lg">PISTA VCX</a>
                <a href="{model_path}ghost-v7.html" class="font-bold text-lg">GHOST V7</a>
                <a href="{model_path}black-street.html" class="font-bold text-lg">BLACK STREET</a>
                <a href="{model_path}power-spring-st.html" class="font-bold text-lg">SPRING ST</a>
                <a href="{model_path}blaster.html" class="font-bold text-lg text-kim-red">BLASTER</a>
                <a href="#" class="font-bold text-lg text-gray-500 cursor-not-allowed">POWER (Bientôt)</a>
"""
    content = mobile_menu_pattern.sub(r'\1' + mobile_items + r'\2', content)

    # --- 3. Fix specific broken images in pista-hr and pista-hr-plus ---
    if 'pista-hr.html' in filepath:
        content = content.replace('../media/pista-hr/kim1.webp', '../media/pista-hr/kim1_1-copie.webp')
        content = content.replace('../media/pista-hr/kim1_Sans titre-2-Récupéré copie.jpg', '../media/pista-hr/kim1_Sans-titre-2-Récupéré-copie.webp')
    
    # General extension fixes
    content = content.replace('.jpg', '.webp')
    content = content.replace('.png', '.webp') # Be careful with favicon and logo? No, logo.png is usually png.
    # Actually, let's only replace extensions for media folders
    content = re.sub(r'media/([^/]+)/([^.]+)\.(jpg|png|jpeg)', r'media/\1/\2.webp', content)

    # Ensure logo.png and favicon.png stay as they are (or webp if they were converted)
    # Based on ls output, I don't see logo.webp or favicon.webp, so I'll revert them if they were changed
    content = content.replace('logo.webp', 'logo.png')
    content = content.replace('favicon.webp', 'favicon.png')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

html_files = glob.glob('*.html') + glob.glob('modeles/*.html')
for f in html_files:
    update_file(f)

