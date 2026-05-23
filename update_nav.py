#!/usr/bin/env python3
"""
update_nav.py  —  KIM Motors
Replaces old nav, loader and mobile-menu in every HTML file with
the new unified dark version that matches index.html.

Run from project root:
    python3 update_nav.py
"""

import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))

# ── helpers ──────────────────────────────────────────────────────────────────
def prefix(in_modeles: bool) -> str:
    return "../" if in_modeles else ""

def loader_html(p: str) -> str:
    return f"""    <!-- Loader (Giant Logo) -->
    <div id="loader" class="fixed inset-0 z-[100] flex items-center justify-center bg-kim-darker transition-opacity duration-700">
        <div class="relative w-3/4 md:w-1/2 max-w-4xl h-auto">
            <img src="{p}media/logo.png" alt="KIM Motors Loading" class="w-full h-auto opacity-10 grayscale">
            <div class="absolute inset-0 overflow-hidden loader-fill">
                <img src="{p}media/logo.png" alt="KIM Motors Loading" class="w-full h-auto max-w-none">
            </div>
        </div>
    </div>"""

def header_html(p: str, in_modeles: bool) -> str:
    # Links differ: root pages use "modeles/x.html", modeles/ pages use "x.html"
    m = "" if in_modeles else "modeles/"
    cat = f"{p}catalogue.html"
    return f"""    <!-- Navbar (Unified) -->
    <header class="absolute w-full z-50 top-0 transition-all duration-300 group" id="navbar">
        <div class="absolute inset-0 bg-transparent transition-all duration-300" id="nav-bg"></div>

        <div class="container mx-auto px-4 lg:px-8 relative">
            <div class="flex items-center justify-between h-24">
                <!-- Logo -->
                <a href="{p}index.html" class="flex items-center shrink-0 z-50 relative transition-transform duration-300 hover:scale-105">
                    <img src="{p}media/logo.png" alt="KIM Motors" class="h-16 md:h-20 w-auto object-contain drop-shadow-xl">
                </a>

                <!-- Desktop Navigation -->
                <nav class="hidden lg:flex items-center space-x-12 absolute left-1/2 transform -translate-x-1/2 z-50">
                    <a href="{p}index.html" class="text-sm font-bold uppercase tracking-widest text-white hover:text-kim-red transition-colors relative after:content-[''] after:absolute after:-bottom-2 after:left-0 after:w-0 after:h-[2px] after:bg-kim-red hover:after:w-full after:transition-all after:duration-300">Accueil</a>
                    <div class="h-24 flex items-center cursor-pointer" id="nav-modeles">
                        <a class="text-sm font-bold uppercase tracking-widest text-white hover:text-kim-red transition-colors flex items-center gap-2 group/menu">
                            Modèles <i class="fa-solid fa-chevron-down text-[10px] group-hover/menu:rotate-180 transition-transform duration-300"></i>
                        </a>
                    </div>
                    <a href="{p}a-propos.html" class="text-sm font-bold uppercase tracking-widest text-white hover:text-kim-red transition-colors relative after:content-[''] after:absolute after:-bottom-2 after:left-0 after:w-0 after:h-[2px] after:bg-kim-red hover:after:w-full after:transition-all after:duration-300">À Propos</a>
                    <a href="{p}atelier.html" class="text-sm font-bold uppercase tracking-widest text-white hover:text-kim-red transition-colors relative after:content-[''] after:absolute after:-bottom-2 after:left-0 after:w-0 after:h-[2px] after:bg-kim-red hover:after:w-full after:transition-all after:duration-300">L'Atelier</a>
                    <a href="{p}contact.html" class="text-sm font-bold uppercase tracking-widest text-white hover:text-kim-red transition-colors relative after:content-[''] after:absolute after:-bottom-2 after:left-0 after:w-0 after:h-[2px] after:bg-kim-red hover:after:w-full after:transition-all after:duration-300">Contact</a>
                </nav>

                <!-- Right Actions -->
                <div class="flex items-center space-x-6 z-50">
                    <a href="{p}devis.html" class="hidden md:flex relative overflow-hidden group/btn px-8 py-3 bg-white/10 backdrop-blur-sm border border-white/20 hover:border-kim-red transition-colors">
                        <div class="absolute inset-0 bg-kim-red transform -translate-x-full group-hover/btn:translate-x-0 transition-transform duration-500 ease-out z-0"></div>
                        <span class="relative z-10 text-xs font-bold uppercase tracking-[0.2em] text-white">Devis</span>
                    </a>
                    <button id="mobile-menu-btn" class="lg:hidden p-2 text-white hover:text-kim-red transition-colors">
                        <div class="w-8 h-[2px] bg-current mb-2"></div>
                        <div class="w-6 h-[2px] bg-current mb-2 ml-auto"></div>
                        <div class="w-8 h-[2px] bg-current"></div>
                    </button>
                </div>
            </div>
        </div>

        <!-- Mega Menu -->
        <div id="mega-menu" class="absolute top-full left-0 w-full bg-kim-darker/98 backdrop-blur-3xl border-t border-b border-gray-800 shadow-2xl overflow-hidden">
            <div class="container mx-auto px-4 py-12">
                <div class="flex justify-between items-end mb-8 border-b border-gray-800 pb-4">
                    <h3 class="text-3xl font-sport font-bold text-white tracking-widest">SÉLECTIONNEZ VOTRE <span class="text-kim-red">MODÈLE</span></h3>
                    <a href="{cat}" class="text-xs font-bold uppercase tracking-widest text-gray-400 hover:text-white flex items-center gap-2">Voir tout le catalogue <i class="fa-solid fa-arrow-right"></i></a>
                </div>
                <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-8 gap-4">
                    <a href="{m}pista-hr.html" class="group relative aspect-[3/4] overflow-hidden bg-black flex items-end p-4">
                        <img src="{p}media/pista-hr/kim1_hr-affiche-2.1.webp" alt="Pista HR" class="absolute inset-0 w-full h-full object-cover opacity-60 group-hover:opacity-100 group-hover:scale-110 transition-all duration-500">
                        <div class="absolute inset-0 bg-gradient-to-t from-black via-black/20 to-transparent"></div>
                        <h4 class="relative z-10 font-sport font-bold text-2xl tracking-wide text-white group-hover:text-kim-red transition-colors">PISTA HR</h4>
                    </a>
                    <a href="{m}pista-hr-plus.html" class="group relative aspect-[3/4] overflow-hidden bg-black flex items-end p-4">
                        <img src="{p}media/pista-hr/kim1_hr-affiche-2.1.webp" alt="Pista HR+" class="absolute inset-0 w-full h-full object-cover opacity-60 group-hover:opacity-100 group-hover:scale-110 transition-all duration-500 filter hue-rotate-90">
                        <div class="absolute inset-0 bg-gradient-to-t from-black via-black/20 to-transparent"></div>
                        <h4 class="relative z-10 font-sport font-bold text-2xl tracking-wide text-white group-hover:text-kim-red transition-colors">PISTA HR+</h4>
                    </a>
                    <a href="{m}pista-vcx.html" class="group relative aspect-[3/4] overflow-hidden bg-black flex items-end p-4">
                        <img src="{p}media/pista-vcx/kim1_PISTA-1.webp" alt="Pista VCX" class="absolute inset-0 w-full h-full object-cover opacity-60 group-hover:opacity-100 group-hover:scale-110 transition-all duration-500">
                        <div class="absolute inset-0 bg-gradient-to-t from-black via-black/20 to-transparent"></div>
                        <h4 class="relative z-10 font-sport font-bold text-2xl tracking-wide text-white group-hover:text-kim-red transition-colors">PISTA VCX</h4>
                    </a>
                    <a href="{m}ghost-v7.html" class="group relative aspect-[3/4] overflow-hidden bg-black flex items-end p-4">
                        <img src="{p}media/ghost-v7/kim2_AFF.webp" alt="Ghost V7" class="absolute inset-0 w-full h-full object-cover opacity-60 group-hover:opacity-100 group-hover:scale-110 transition-all duration-500">
                        <div class="absolute inset-0 bg-gradient-to-t from-black via-black/20 to-transparent"></div>
                        <h4 class="relative z-10 font-sport font-bold text-2xl tracking-wide text-white group-hover:text-kim-red transition-colors">GHOST V7</h4>
                    </a>
                    <a href="{m}black-street.html" class="group relative aspect-[3/4] overflow-hidden bg-black flex items-end p-4">
                        <img src="{p}media/black-street/kim1_DSC06092.webp" alt="Black Street" class="absolute inset-0 w-full h-full object-cover opacity-60 group-hover:opacity-100 group-hover:scale-110 transition-all duration-500">
                        <div class="absolute inset-0 bg-gradient-to-t from-black via-black/20 to-transparent"></div>
                        <h4 class="relative z-10 font-sport font-bold text-2xl tracking-wide text-white group-hover:text-kim-red transition-colors">BLACK STREET</h4>
                    </a>
                    <a href="{m}power-spring-st.html" class="group relative aspect-[3/4] overflow-hidden bg-black flex items-end p-4">
                        <img src="{p}media/power-spring-st/kim3_affiche-spring.webp" alt="Power Spring ST" class="absolute inset-0 w-full h-full object-cover opacity-60 group-hover:opacity-100 group-hover:scale-110 transition-all duration-500">
                        <div class="absolute inset-0 bg-gradient-to-t from-black via-black/20 to-transparent"></div>
                        <h4 class="relative z-10 font-sport font-bold text-2xl tracking-wide text-white group-hover:text-kim-red transition-colors">SPRING ST</h4>
                    </a>
                    <a href="{m}blaster.html" class="group relative aspect-[3/4] overflow-hidden bg-black flex items-end p-4">
                        <img src="{p}media/blaster/kim3_affiche-blaster-copie.webp" alt="Blaster" class="absolute inset-0 w-full h-full object-cover opacity-60 group-hover:opacity-100 group-hover:scale-110 transition-all duration-500">
                        <div class="absolute inset-0 bg-gradient-to-t from-black via-black/20 to-transparent"></div>
                        <h4 class="relative z-10 font-sport font-bold text-2xl tracking-wide text-white group-hover:text-kim-red transition-colors">BLASTER</h4>
                    </a>
                    <a href="{m}power.html" class="group relative aspect-[3/4] overflow-hidden bg-black flex items-end p-4 border border-kim-red">
                        <img src="{p}media/power/110/rouge-vur-globale.webp" alt="Power" class="absolute inset-0 w-full h-full object-cover opacity-60 group-hover:opacity-100 group-hover:scale-110 transition-all duration-500">
                        <div class="absolute inset-0 bg-gradient-to-t from-black via-black/20 to-transparent"></div>
                        <h4 class="relative z-10 font-sport font-bold text-2xl tracking-wide text-kim-red">POWER</h4>
                    </a>
                </div>
            </div>
        </div>
    </header>

    <!-- Mobile Menu -->
    <div id="mobile-menu" class="fixed inset-0 z-40 bg-kim-darker/98 backdrop-blur-3xl transform translate-x-full transition-transform duration-500 pt-24 px-8 lg:hidden flex flex-col overflow-y-auto pb-10">
        <a href="{p}index.html" class="mobile-link text-4xl font-sport font-bold tracking-widest border-b border-gray-800 py-6 text-kim-red">ACCUEIL</a>
        <div class="py-6 border-b border-gray-800">
            <span class="text-sm font-bold tracking-[0.2em] text-gray-500 mb-6 block uppercase">Nos Modèles</span>
            <div class="grid grid-cols-1 gap-4">
                <a href="{m}pista-hr.html" class="font-sport text-3xl font-bold text-white hover:text-kim-red flex justify-between items-center group">PISTA HR <i class="fa-solid fa-arrow-right text-sm opacity-0 group-hover:opacity-100 transition-opacity"></i></a>
                <a href="{m}pista-hr-plus.html" class="font-sport text-3xl font-bold text-white hover:text-kim-red flex justify-between items-center group">PISTA HR+ <i class="fa-solid fa-arrow-right text-sm opacity-0 group-hover:opacity-100 transition-opacity"></i></a>
                <a href="{m}pista-vcx.html" class="font-sport text-3xl font-bold text-white hover:text-kim-red flex justify-between items-center group">PISTA VCX <i class="fa-solid fa-arrow-right text-sm opacity-0 group-hover:opacity-100 transition-opacity"></i></a>
                <a href="{m}ghost-v7.html" class="font-sport text-3xl font-bold text-white hover:text-kim-red flex justify-between items-center group">GHOST V7 <i class="fa-solid fa-arrow-right text-sm opacity-0 group-hover:opacity-100 transition-opacity"></i></a>
                <a href="{m}black-street.html" class="font-sport text-3xl font-bold text-white hover:text-kim-red flex justify-between items-center group">BLACK STREET <i class="fa-solid fa-arrow-right text-sm opacity-0 group-hover:opacity-100 transition-opacity"></i></a>
                <a href="{m}power-spring-st.html" class="font-sport text-3xl font-bold text-white hover:text-kim-red flex justify-between items-center group">SPRING ST <i class="fa-solid fa-arrow-right text-sm opacity-0 group-hover:opacity-100 transition-opacity"></i></a>
                <a href="{m}blaster.html" class="font-sport text-3xl font-bold text-white hover:text-kim-red flex justify-between items-center group">BLASTER <i class="fa-solid fa-arrow-right text-sm opacity-0 group-hover:opacity-100 transition-opacity"></i></a>
                <a href="{m}power.html" class="font-sport text-3xl font-bold text-white hover:text-kim-red flex justify-between items-center group">POWER <i class="fa-solid fa-arrow-right text-sm opacity-0 group-hover:opacity-100 transition-opacity"></i></a>
            </div>
        </div>
        <a href="{p}a-propos.html" class="mobile-link text-4xl font-sport font-bold tracking-widest border-b border-gray-800 py-6 text-white hover:text-kim-red">À PROPOS</a>
        <a href="{p}atelier.html" class="mobile-link text-4xl font-sport font-bold tracking-widest border-b border-gray-800 py-6 text-white hover:text-kim-red">L'ATELIER</a>
        <a href="{p}contact.html" class="mobile-link text-4xl font-sport font-bold tracking-widest py-6 text-white hover:text-kim-red">CONTACT</a>
        <button id="close-mobile-menu" class="absolute top-6 right-6 p-4 text-white">
            <i class="fa-solid fa-xmark text-4xl"></i>
        </button>
    </div>"""

# ── regex patterns for the blocks we want to remove ──────────────────────────
# We match everything from the opening of <div id="loader"...> to the closing </div>
LOADER_PATTERN = re.compile(
    r'[ \t]*<!--\s*Loader.*?-->\s*\n[ \t]*<div id="loader".*?</div>\s*\n(?:\s*</div>\s*\n)?',
    re.DOTALL | re.IGNORECASE
)

# Match <header ... id="navbar"...> ... </header>
HEADER_PATTERN = re.compile(
    r'[ \t]*<header\b[^>]*id=["\']navbar["\'][^>]*>.*?</header>',
    re.DOTALL | re.IGNORECASE
)

# Match the mobile menu div
MOBILE_MENU_PATTERN = re.compile(
    r'[ \t]*<!--\s*Mobile Menu\s*-->\s*\n[ \t]*<div id="mobile-menu".*?</div>\s*\n(?=\s*(?:<main|<section|<div|<!--|$))',
    re.DOTALL | re.IGNORECASE
)

def process_file(path: str):
    in_modeles = path.startswith(os.path.join(ROOT, 'modeles'))
    p = prefix(in_modeles)

    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    original = html

    # 1. Replace loader
    html = LOADER_PATTERN.sub('', html)

    # 2. Replace header+mega-menu block
    html = HEADER_PATTERN.sub('', html)

    # 3. Replace old mobile-menu div
    html = MOBILE_MENU_PATTERN.sub('', html)

    # 4. Insert new blocks after <body ...>
    # We look for <body and insert right after the closing >
    body_tag = re.search(r'(<body\b[^>]*>)', html)
    if body_tag:
        insert_at = body_tag.end()
        new_loader = '\n' + loader_html(p) + '\n'
        new_nav = '\n' + header_html(p, in_modeles) + '\n'
        html = html[:insert_at] + new_loader + new_nav + html[insert_at:]

    if html != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  ✅ Updated: {os.path.relpath(path, ROOT)}")
    else:
        print(f"  ⚠️  No change: {os.path.relpath(path, ROOT)}")

# ── main ─────────────────────────────────────────────────────────────────────
SKIP_FILES = set()  # Sync all files to propagate the active POWER link

print("\n🔧 KIM Motors — Updating nav + loader on all pages…\n")

for dirpath, _, filenames in os.walk(ROOT):
    # Skip node_modules or hidden dirs
    if any(p.startswith('.') for p in dirpath.split(os.sep)):
        continue
    for fname in filenames:
        if not fname.endswith('.html'):
            continue
        rel = os.path.relpath(os.path.join(dirpath, fname), ROOT)
        if fname in SKIP_FILES:
            print(f"  ⏭️  Skipped: {rel}")
            continue
        process_file(os.path.join(dirpath, fname))

print("\n✅ Done.\n")
