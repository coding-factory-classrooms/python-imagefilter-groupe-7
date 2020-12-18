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

    cmd = f'python main.py -i {config["general"]["input_dir"]} -o {config["general"]["output_dir"]} --filters "{config["filters"]["content"]}"'
    os.system(cmd)