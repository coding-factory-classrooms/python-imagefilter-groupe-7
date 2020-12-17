import sys
import cv2
import os
import logger

from filters import gaussianblur, grayscale, dilate


args = sys.argv # Liste des arguments
for i in range(0, len(args)):
    arg = args[i]
    print(f'{arg}')

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



        else:
            print('Chemin incorrect')

    if arg == '--filters':
        for f in files:
            try:
                file_path = f"{input_dir}/{f}"  # Va cherche un element de la liste à chaque tour de boucle
                image = cv2.imread(file_path)
                logger.log_in_file(f'Opening image = ' + file_path)
                        # récupère l'image de base

                filters = args[i + 1]
                split_filters = filters.split("|")
                print(split_filters)
                for s in split_filters:
                    # Application des filtres
                    print(s)
                    if 'blur' in s:
                        split_filter = s.split(":")
                        value = split_filter[1]
                        value_int = int(value)
                        image = gaussianblur.filter_blur(image,value_int)
                        print('blur on')
                    if 'dilate' in s:
                        split_filter = s.split(":")
                        value = split_filter[1]
                        value_int = int(value)
                        image = dilate.filter_dilate(image, value_int)
                        print('dilate on')
                    if 'grayscale' in s:
                        image = grayscale.filter_grayscale(image)
                        print('grayscale on')

                # Enregistrer l'image filtrée dans le dossier de sortie voulu
                file_exit_path = f'{path_output}/{f}'
                cv2.imwrite(file_exit_path, image)
                logger.log_in_file(f'Save result image to image = ' + file_exit_path)
            except cv2.error as e:
                print(e)
            except NameError as e:
                print(e)
logger.print_log_in_console()