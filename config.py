from configparser import ConfigParser
import os
def apply_config(path_ini):
    """
    :param path_ini: Le nom du fichier ini récuperé
    Récupère les valeurs du fichier ini grâce à configparser et les lit
    Ligne de commande avec le fichier ini
    Applique cette ligne de commande dans le terminal grâce a os.system()

    """
    file = path_ini
    config = ConfigParser()
    config.read(file)


    input = f'-i {config["general"]["input_dir"]}'
    output = f'-o {config["general"]["output_dir"]}'
    filters = f'--filters "{config["filters"]["content"]}"'

    cmd = f'python main.py {input} {output} {filters}'

    os.system(cmd)