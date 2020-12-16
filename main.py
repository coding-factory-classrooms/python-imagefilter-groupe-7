import cv2
import os

from filters import gaussianblur, grayscale, dilate

input_dir = 'data/img' # Chemin dossier 'img'
files = os.listdir(input_dir) # Retourne une liste de ce qui se trouve dans le dossier 'img'
for f in files:
    try:
        file_path = f"{input_dir}/{f}" # Va cherche un element de la liste à chaque tour de boucle
        # récupère l'image de base
        image = cv2.imread(file_path)

        #Application des filtres

        image = gaussianblur.filter_blur(image)
        image = grayscale.filter_grayscale(image)
        image = dilate.filter_dilate(image)

        #Enregistrer l'image filtrée dans le dossier de sortie
        cv2.imwrite(f'data/output/{f}', image)
    # Attrape erreur cv2
    except cv2.error as e:
        print(e)