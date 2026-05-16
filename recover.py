import os
import shutil

original_files = """
media/kim1sur3/blackstreet/DSC06092.jpg
media/kim1sur3/kim1.mp4
media/kim1sur3/pista vcx/PISTA 1.jpg
media/kim1sur3/pista vcx/DSC06228.jpg
media/kim1sur3/pista vcx/Séquence 01.00_00_25_19.Still004.png
media/kim1sur3/pista vcx/Séquence 01.00_00_47_11.Still009.png
media/kim1sur3/pista vcx/Séquence 01.00_00_14_23.Still008.png
media/kim1sur3/pista vcx/DSC06229.jpg
media/kim1sur3/pista vcx/PISTA 2.jpg
media/kim1sur3/pista vcx/DSC06174.jpg
media/kim1sur3/pista vcx/IMG_20240605_223239.jpg
media/kim1sur3/pista vcx/pista 3.jpg
media/kim1sur3/pista vcx/Séquence 01.00_00_14_05.Still003.png
media/kim1sur3/pista vcx/DSC06164.jpg
media/kim1sur3/pista vcx/Séquence 01.00_00_22_25.Still007.png
media/kim1sur3/pista vcx/pista 17.jpg
media/kim1sur3/pista vcx/Séquence 01.00_00_27_23.Still005.png
media/kim1sur3/pista vcx/IMG_20240419_211601.jpg
media/kim1sur3/pista vcx/DSC06221.jpg
media/kim1sur3/pista vcx/DSC06180.jpg
media/kim1sur3/pista vcx/Séquence 01.00_00_33_09.Still006.png
media/kim1sur3/pista vcx/DSC06227.jpg
media/kim1sur3/pista vcx/DSC06233.jpg
media/kim1sur3/pista vcx/Séquence 01.00_00_00_26.Still002.png
media/kim1sur3/pista vcx/Séquence 03.mp4
media/kim1sur3/pista vcx/DSC06179.jpg
media/kim1sur3/pista vcx/DSC06232.jpg
media/kim1sur3/pista vcx/FICHE TECHNIQUE PISTA VCX..jpg
media/kim1sur3/pista vcx/DSC06231.jpg
media/kim1sur3/pista hr+/DSC06957.png
media/kim1sur3/pista hr/3 copie.jpg
media/kim1sur3/pista hr/PANO PISTA HR..jpg
media/kim1sur3/pista hr/1732053169278.jpg
media/kim1sur3/pista hr/Intro Slideshow.mov
media/kim1sur3/pista hr/1732053098243.jpg
media/kim1sur3/pista hr/1732053272627.jpg
media/kim1sur3/pista hr/DSC00050.ARW
media/kim1sur3/pista hr/hr affiche 2.1.jpg
media/kim1sur3/pista hr/1732053076919.jpg
media/kim1sur3/pista hr/1732053598005.jpg
media/kim1sur3/pista hr/caracterestique PISTA HR.jpg
media/kim1sur3/pista hr/1 copie.jpg
media/kim1sur3/pista hr/1732053127625.jpg
media/kim1sur3/pista hr/1732053185532.jpg
media/kim1sur3/pista hr/tun.jpg
media/kim1sur3/pista hr/1732053056027.jpg
media/kim1sur3/pista hr/81.jpg
media/kim1sur3/pista hr/Sans titre-2-Récupéré copie.jpg
media/kim2sur3/blackstreet/DSC06116.jpg
media/kim2sur3/blackstreet/DSC06082.png
media/kim2sur3/blackstreet/4.jpeg
media/kim2sur3/blackstreet/14.jpeg
media/kim2sur3/blackstreet/DSC06124.jpg
media/kim2sur3/blackstreet/DSC06020.jpg
media/kim2sur3/kim2.mp4
media/kim2sur3/ghost v7/gosst copie.jpg
media/kim2sur3/ghost v7/DSC05685.JPG
media/kim2sur3/ghost v7/GH R.jpg
media/kim2sur3/ghost v7/GHOSTvert.jpg
media/kim2sur3/ghost v7/#INTRO SLIDESHOW v03.mov
media/kim2sur3/ghost v7/ghost rouge affiche.png
media/kim2sur3/ghost v7/ghost blanc .png
media/kim2sur3/ghost v7/blanc.jpg
media/kim2sur3/ghost v7/BLEU K.jpg
media/kim2sur3/ghost v7/AFF.jpg
media/kim2sur3/ghost v7/GHOST bleu.jpg
media/kim2sur3/ghost v7/C0566T01 copie.jpg
media/kim2sur3/KIM/pista logo officiel.png
media/kim2sur3/KIM/SPRING ST.png
media/kim2sur3/KIM/logo.png
media/kim2sur3/KIM/HR.png
media/kim3sur3/blackstreet/DSC06016.jpg
media/kim3sur3/blackstreet/DSC06002.jpg
media/kim3sur3/blackstreet/DSC06002.png
media/kim3sur3/blackstreet/DSC06028.jpg
media/kim3sur3/blackstreet/DSC06007.jpg
media/kim3sur3/blackstreet/DSC06012.jpg
media/kim3sur3/blackstreet/DSC06114.jpg
media/kim3sur3/blackstreet/DSC06100.jpg
media/kim3sur3/blackstreet/DSC06074.jpg
media/kim3sur3/blackstreet/DSC06076.jpg
media/kim3sur3/blackstreet/DSC09556.jpg
media/kim3sur3/blackstreet/fire 2.png
media/kim3sur3/blackstreet/DSC06009-Edit.jpg
media/kim3sur3/blackstreet/spot light.png
media/kim3sur3/blackstreet/2-Edit-Récupéré copie.jpg
media/kim3sur3/blackstreet/DSC06111.jpg
media/kim3sur3/blackstreet/DSC06071.jpg
media/kim3sur3/blackstreet/DSC06120.jpg
media/kim3sur3/blackstreet/DSC06069.jpg
media/kim3sur3/blackstreet/DSC06056.jpg
media/kim3sur3/blackstreet/DSC06091.jpg
media/kim3sur3/blackstreet/white + design copie.png
media/kim3sur3/blackstreet/11-Edit.tif
media/kim3sur3/blackstreet/9-Edit.tif
media/kim3sur3/blackstreet/DSC09558.jpg
media/kim3sur3/blackstreet/2-Edi2t_01_01 copie.jpg
media/kim3sur3/blackstreet/Arrière-plan copie.jpg
media/kim3sur3/spring st/AMIR MOTO Timeline 1 (Resolve).00_00_52_30.Still010.jpg
media/kim3sur3/spring st/960-480.mp4
media/kim3sur3/spring st/AMIR MOTO Timeline 1 (Resolve).00_00_42_51.Still008.jpg
media/kim3sur3/spring st/640-240.mp4
media/kim3sur3/spring st/spot moto Final25.jpg
media/kim3sur3/spring st/spot moto Final21 copie.jpg
media/kim3sur3/spring st/1536-576.mp4
media/kim3sur3/spring st/640-480.mp4
media/kim3sur3/spring st/spot moto Final36.jpg
media/kim3sur3/spring st/AMIR MOTO Timeline 1 (Resolve).00_00_39_41.Still007 copie.jpg
media/kim3sur3/spring st/AMIR MOTO Timeline 1 (Resolve).00_00_23_09.Still001 copie.jpg
media/kim3sur3/spring st/1124-576.mp4
media/kim3sur3/spring st/AMIR MOTO Timeline 1 (Resolve).00_00_51_04.Still009.jpg
media/kim3sur3/spring st/432  576.mp4
media/kim3sur3/spring st/4.jpg
media/kim3sur3/spring st/576-432.mp4
media/kim3sur3/spring st/affiche spring.jpg
media/kim3sur3/spring st/1.jpg
media/kim3sur3/spring st/032.jpg
media/kim3sur3/spring st/47a3c158-232b-4797-83a4-e094d52222f7.jpeg
media/kim3sur3/blaster/blaster vert copie.jpg
media/kim3sur3/blaster/blaster noir copie.jpg
media/kim3sur3/blaster/vert  copie.jpg
media/kim3sur3/blaster/blaster rouge  copie.jpg
media/kim3sur3/blaster/affiche blaster copie.jpg
media/kim3sur3/blaster/BLASTER PRIX copie.jpg
media/kim3sur3/pista hr+/DSC06770.jpg
media/kim3sur3/pista hr+/HR+ NV 2026 Bleu métallisé.png
media/kim3sur3/pista hr+/DSC07093.png
media/kim3sur3/pista hr+/HR+ NV 2026 noir rouge.png
media/kim3sur3/pista hr+/DSC06739.png
media/kim3sur3/pista hr+/HR+ NV 2026 vert.png
media/kim3sur3/pista hr+/DSC07025.png
media/kim3sur3/pista hr+/HR+ NV rouge.png
media/kim3sur3/pista hr+/lv_7597062072395992336_20260215004226.mp4
media/kim3sur3/pista hr+/lv_7488913730302922037_20260215011136.mp4
media/kim3sur3/pista hr+/lv_7536425777248701749_20250914141229.mp4
media/kim3sur3/pista hr+/HR+ NV 2026 noir carbon.png
media/kim3sur3/pista hr/DSC00049.JPG
media/kim3sur3/pista hr/1732053156338.jpg
media/kim3sur3/pista hr/5 copie.jpg
media/kim3sur3/pista hr/8 copie.jpg
media/kim3sur3/pista hr/HR ROUGE.jpg
media/kim3sur3/pista hr/133472048_Mega Sale-10 copie.jpg
media/kim3sur3/pista hr/Sans titre-2-Récupéré.jpg
media/kim3sur3/pista hr/7 copie.jpg
media/kim3sur3/pista hr/4.jpg
media/kim3sur3/pista hr/1732053319880.jpg
media/kim3sur3/pista hr/nouvel arrivage pista hr.jpg
media/kim3sur3/pista hr/DSC00044.JPG
media/kim3sur3/pista hr/3.jpg
media/kim3sur3/ghost v7/carbon.png
media/kim3sur3/ghost v7/GHOST blanc.jpg
media/kim3sur3/ghost v7/GHOST CARBON.png
media/kim3sur3/ghost v7/vert.jpg
media/kim3sur3/ghost v7/ghost v7 vert.png
media/kim3sur3/ghost v7/GHOST AFFICHE NOIR NOIR.png
media/kim3sur3/ghost v7/DSC05710-Récupéré copie.jpg
media/kim3sur3/ghost v7/ghost vert affiche copie.png
media/kim3sur3/ghost v7/GHOST BLEU.png
media/kim3sur3/ghost v7/motro copie.jpg
media/kim3sur3/ghost v7/DSC05716.JPG
media/kim3sur3/ghost v7/rouge.jpg
media/kim3sur3/KIM/blackstreet.png
media/kim3sur3/KIM/logo-groupe.png
media/kim3sur3/KIM/vcx.png
media/kim3sur3/KIM/power.png
media/kim3sur3/KIM/BLASTER.png
media/kim3sur3/KIM/hr+.png
media/kim3sur3/KIM/22.png
media/kim3sur3/KIM/ghost v7.png
media/kim3sur3/KIM/ghost v10.png
media/kim3sur3/KIM/square.png
"""

slug_map = {
    'blackstreet': 'black-street',
    'pista vcx': 'pista-vcx',
    'pista hr+': 'pista-hr-plus',
    'pista hr': 'pista-hr',
    'ghost v7': 'ghost-v7',
    'KIM': 'kim-group',
    'spring st': 'power-spring-st',
    'blaster': 'blaster'
}

for line in original_files.strip().split('\n'):
    parts = line.split('/')
    if len(parts) >= 3:
        source_group = parts[1] # kim1sur3
        prefix = source_group.replace('sur3', '') # kim1
        
        if len(parts) == 3:
            # File directly in kim1sur3 (like kim1.mp4)
            filename = parts[2]
            dest_dir = "media/kim-group"
        else:
            parent_dir = parts[2]
            filename = parts[3]
            dest_dir = "media/" + slug_map.get(parent_dir, parent_dir.lower().replace(' ', '-').replace('+','-plus'))
        
        current_path = f"media/{prefix}_{filename}"
        
        if os.path.exists(current_path):
            os.makedirs(dest_dir, exist_ok=True)
            # Use original filename to revert the prefix rename, unless there is a collision
            # Wait, the user said "appelle les comme tu veux", so we can keep the prefix to be perfectly safe
            # from collisions. Let's keep the prefix: kim1_filename.jpg
            dest_path = f"{dest_dir}/{prefix}_{filename}"
            shutil.move(current_path, dest_path)
            print(f"Moved {current_path} to {dest_path}")
        else:
            # Check if it was already moved without prefix?
            if os.path.exists(f"media/{filename}"):
                os.makedirs(dest_dir, exist_ok=True)
                dest_path = f"{dest_dir}/{prefix}_{filename}"
                shutil.move(f"media/{filename}", dest_path)
                print(f"Moved media/{filename} to {dest_path}")

print("Done recovering files.")
