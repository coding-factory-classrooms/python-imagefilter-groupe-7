import sys
import cv2
import os
import logger

from filters import gaussianblur, grayscale, dilate
import config

args = sys.argv # Liste des arguments
for i in range(0, len(args)):
    try:
        arg = args[i]

        #HELP
        if arg == '-h':
            print('--help')
            sys.exit()

        # List filters (version du pauvre)
        if arg == '--list-filters':
            print('List of supported filters\nblur\ndilate\ngrayscale')
            sys.exit()

        #CONFIG INI
        if arg == '--config-file':
            path_ini = args[i + 1]
            config.apply_config(path_ini)

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
    except IndexError as e:
        print(e)

    if arg == '--filters':
        for f in files:
            try:
                file_path = f"{input_dir}/{f}"  # Va cherche un element de la liste à chaque tour de boucle
                image = cv2.imread(file_path)
                logger.log_in_file(f'Opening image = ' + file_path)
                        # récupère l'image de base

                filters = args[i + 1]
                split_filters = filters.split("|")
                for s in split_filters:
                    # Application des filtres
                    if 'blur' in s:
                        split_filter = s.split(":")
                        value = split_filter[1]
                        value_int = int(value)
                        image = gaussianblur.filter_blur(image,value_int)
                    if 'dilate' in s:
                        split_filter = s.split(":")
                        value = split_filter[1]
                        value_int = int(value)
                        image = dilate.filter_dilate(image, value_int)
                    if 'grayscale' in s:
                        image = grayscale.filter_grayscale(image)

                # Enregistrer l'image filtrée dans le dossier de sortie voulu
                file_exit_path = f'{path_output}/{f}'
                cv2.imwrite(file_exit_path, image)
                logger.log_in_file(f'Save result image to image = ' + file_exit_path)
            except cv2.error as e:
                print(e)
            except NameError as e:
                print(e)
            except IndexError as e:
                print(e)
try:
    logger.print_log_in_console()
except FileNotFoundError as e:
    print(e)