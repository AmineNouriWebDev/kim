import re
import glob

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to replace the broken block in the desktop nav.
    # The broken block looks like:
    #                         </a>
    #                 <a href="#" class="font-bold text-lg text-gray-500 cursor-not-allowed">POWER (Bientôt)</a>
    #             </div>
    #         </div>
    #         <a href="[../]*a-propos.html" class="hover-underline ...">À Propos</a>
    #
    # We want to restore it to:
    #                         </a>
    #                     </div>
    #                     <a href="[../]*a-propos.html" class="hover-underline ...">À Propos</a>

    pattern = re.compile(
        r'(<a href="#" class="hover-underline text-sm font-bold uppercase tracking-widest[^>]+flex items-center gap-2">\s*Modèles <i class="fa-solid fa-chevron-down text-xs"></i>\s*</a>)\s*<a href="#" class="font-bold text-lg text-gray-500 cursor-not-allowed">POWER \(Bientôt\)</a>\s*</div>\s*</div>\s*<a href="((?:\.\./)?a-propos\.html)"',
        re.MULTILINE
    )

    def replacement(match):
        a_modeles = match.group(1)
        href_apropos = match.group(2)
        return f'{a_modeles}\n                    </div>\n                    <a href="{href_apropos}"'

    new_content, count = pattern.subn(replacement, content)

    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed desktop nav in {filepath}")
    else:
        print(f"No changes in {filepath}")

html_files = glob.glob('*.html') + glob.glob('modeles/*.html')
for f in html_files:
    fix_file(f)

