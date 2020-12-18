from configparser import ConfigParser
import os
def apply_config(path_ini):
    """

    :param path_ini:

    """
    file = path_ini
    config = ConfigParser()
    config.read(file)

    cmd = f'python main.py -i {config["general"]["input_dir"]} -o {config["general"]["output_dir"]} --filters "{config["filters"]["content"]}"'
    os.system(cmd)