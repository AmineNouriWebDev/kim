import re

with open('modeles/pista-hr-plus.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix table wrapper
content = content.replace(
    '<div class="max-w-3xl mx-auto overflow-hidden rounded-3xl border border-gray-800">',
    '<div class="max-w-3xl mx-auto overflow-x-auto rounded-3xl border border-gray-800">'
)

# Fix table text size
content = content.replace(
    '<table class="w-full text-sm">',
    '<table class="w-full text-[10px] md:text-sm">'
)

# Fix paddings in the table header
content = content.replace(
    '<th class="text-left py-4 px-8',
    '<th class="text-left py-3 px-3 md:py-4 md:px-8'
)

# Fix text size in table header
content = content.replace(
    'tracking-widest text-xs">Caractéristique',
    'tracking-widest text-[9px] md:text-xs">Caractéristique'
)
content = content.replace(
    'tracking-widest text-xs">Détail',
    'tracking-widest text-[9px] md:text-xs">Détail'
)

# Fix paddings in all cells
# We will use regex to only replace it inside the tbody of the table
# The table is in SECTION 7
specs_start = content.find('<!-- ===== SECTION 7: SPECS TABLE ===== -->')
specs_content = content[specs_start:]

# Replace `py-4 px-8` with `py-2 px-3 md:py-4 md:px-8` in the table
specs_content = specs_content.replace('py-4 px-8', 'py-2 px-3 md:py-4 md:px-8')

content = content[:specs_start] + specs_content

with open('modeles/pista-hr-plus.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done fixing table sizes on pista-hr-plus.html")
