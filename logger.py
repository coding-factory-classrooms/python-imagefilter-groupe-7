import sys
from datetime import datetime


log_file = 'operations.log' # Création fichier log par défaut

args = sys.argv
for i in range(0, len(args)):
    arg = args[i]
    if arg == '--log-file': # Vérifie si '--log-file' est présent
        name_log = args[i + 1] # récupère le nom du fichier log qui suit '--log-file'
        log_file = name_log  #Ecrase le nom du fichier log par defaut par celui fourni

def log_in_file(msg):
    now = datetime.now()
    timestamp = now.strftime('%Y/%m/%d %H:%M')
    with open(log_file, 'a') as f:
        f.write(f'{timestamp} - {msg}' + '\n')


def print_log_in_console():
    with open(log_file, 'r') as f:
        print(f.read())
