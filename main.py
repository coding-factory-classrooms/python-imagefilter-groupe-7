import sys
import cv2
import os

from filters import gaussianblur, grayscale, dilate


args = sys.argv # Liste des arguments
for i in range(0, len(args)):
    arg = args[i]
    if arg == '-h':
        print('HELP')
    # OUTPUT
    if arg == '-o':
        path_output = args[i + 1] # Prends l'argument qui suit le '-o'
        if os.path.exists(path_output) == False: # Vérifie que le dossier n'existe pas
            os.makedirs(path_output) # Si il n'existe pas, le crée

    #INPUT
    if arg == '-i':
        path_input = args[i + 1] # Prends l'argument qui suit le '-i'
        if os.path.exists(path_input): # Vérifie que le dossier existe
            input_dir = path_input  # Chemin dossier 'input'
            files = os.listdir(input_dir)  # Retourne une liste de ce qui se trouve dans le dossier 'input'
            for f in files:

                try:
                    file_path = f"{input_dir}/{f}" # Va cherche un element de la liste à chaque tour de boucle
                    # récupère l'image de base
                    image = cv2.imread(file_path)

                    #Application des filtres

                    image = gaussianblur.filter_blur(image)
                    image = grayscale.filter_grayscale(image)
                    image = dilate.filter_dilate(image)

                    #Enregistrer l'image filtrée dans le dossier de sortie voulu
                    cv2.imwrite(f'{path_output}/{f}', image)
                # Attrape erreur cv2
                except cv2.error as e:
                    print(e)
        else:
            print('Chemin incorrect')