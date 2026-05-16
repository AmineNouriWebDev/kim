import os

files_to_update = [
    'index.html', 'atelier.html', 'contact.html', 'devis.html', 'a-propos.html',
    'modeles/pista-hr.html', 'modeles/pista-hr-plus.html', 'modeles/pista-vcx.html',
    'modeles/ghost-v7.html', 'modeles/black-street.html', 'modeles/power-spring-st.html',
    'modeles/power-125.html', 'modeles/power-110.html', 'modeles/blaster.html',
    'assets/js/data.js'
]

path_replacements = {
    'media/kim1sur3/pista hr/hr affiche 2.1.jpg': 'media/pista-hr/kim1_hr affiche 2.1.jpg',
    'media/kim2sur3/ghost v7/AFF.jpg': 'media/ghost-v7/kim2_AFF.jpg',
    'media/kim3sur3/blaster/affiche blaster copie.jpg': 'media/blaster/kim3_affiche blaster copie.jpg',
    'media/kim1sur3/pista vcx/PISTA 1.jpg': 'media/pista-vcx/kim1_PISTA 1.jpg',
    'media/kim3sur3/blackstreet/DSC06092.jpg': 'media/black-street/kim3_DSC06092.jpg',
    'media/kim3sur3/spring st/affiche spring.jpg': 'media/power-spring-st/kim3_affiche spring.jpg',
    'media/kim2sur3/KIM/logo.png': 'media/kim-group/logo-groupe-kaddeche.png',
}

for file_path in files_to_update:
    if not os.path.exists(file_path): continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for old, new in path_replacements.items():
        if file_path.startswith('modeles/'):
            content = content.replace('../' + old, '../' + new)
        else:
            content = content.replace(old, new)
            
    # Add favicon
    favicon_str = '<link rel="icon" type="image/png" href="../media/favicon.png">' if file_path.startswith('modeles/') else '<link rel="icon" type="image/png" href="media/favicon.png">'
    
    if '<title>' in content and 'favicon.png' not in content:
        content = content.replace('</title>', '</title>\n    ' + favicon_str)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Update completed.")
