import cv2
import os
import logger

from filters import gaussianblur, grayscale, dilate

input_dir = 'data/img' # Chemin dossier 'img'
output_dir = 'data/output' #chemin dossier 'img'sortie
files = os.listdir(input_dir) # Retourne une liste de ce qui se trouve dans le dossier 'img'
for f in files:
    try:
        file_path = f"{input_dir}/{f}" # Va chercher un element de la liste à chaque tour de boucle
        # récupère l'image de base
        image = cv2.imread(file_path)
        logger.log_in_file(f'Opening image = ' + file_path)

        #Application des filtres

        image = gaussianblur.filter_blur(image)
        image = grayscale.filter_grayscale(image)
        image = dilate.filter_dilate(image)

        #Enregistrer l'image filtrée dans le dossier de sortie

        file_exit_path = f'{output_dir}/{f}'
        cv2.imwrite(file_exit_path, image)
        logger.log_in_file(f'Save result image to image = ' + file_exit_path)

    # Attrape erreur cv2
    except cv2.error as e:
        print(e)


logger.print_log_in_console()