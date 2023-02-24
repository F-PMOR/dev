#!/bin/env python3
import os, sys
from PIL import Image

# Répertoire des images à traiter
#source_dir = '/srv/sda/Multimedia/cadre_numerique'
source_dir = '/srv/sda/Multimedia/test'
#source_dir = './test'

# Répertoire de destination des images redimensionnées
dest_dir = source_dir + "/small"
# Répertoire de destination des images traitées
done_dir = source_dir + "/done"

# images size
largeur, hauteur = 1024, 683

# creation d'une image noire pour le fond de la taille indiquée ci dessus.
backgroundImage=Image.new('RGB',(largeur, hauteur))

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)
if not os.path.exists(done_dir):
    os.makedirs(done_dir)

# Parcourir tous les fichiers dans le répertoire source
for file in os.listdir(source_dir):
    # Ne traiter que les fichiers d'images
    if file.endswith('.jpg') or file.endswith('.png'):
        try: 
            # Charger l'image
            image = Image.open(os.path.join(source_dir, file))
            imageInfo = image.info
            print(f"image info : {imageInfo}")
            # on recupère les dimension de l'image et on l'affiche
            width, height = image.size
            print(f"image {file} : largeur {width} hauteur {height}") 
             
            # Redimensionner l'image
            image = image.resize((largeur, hauteur))
            # si la largeur est inférieur à la hauteure on tourne l'image
            if (int(width) < int(height)):
                print("la largeur est inférieur à la hauteur")
                new_image=image.rotated(angle=90)
                image=backgroundImage.paste(new_image, (50, 50))
            else: 
                # Enregistrer l'image redimensionnée dans le répertoire de destination
                image.save(os.path.join(dest_dir, file))
            try:
                # deplace l'image dans le repertoire des images traitées
                os.rename(os.path.join(source_dir, file),os.path.join(done_dir, file))
            except: 
                print('Erreur de deplacement du fichier, on quitte le programme')
                sys.exit(1)
        except: 
            print("erreur de modification de l'image")
            sys.exit(1)


