from datetime import datetime
log_file = 'opperations.log'

def log_in_file(msg):
    now = datetime.now()
    timestamp = now.strftime('%Y/%m/%d %H:%M')
    with open(log_file, 'a') as f:
        f.write(f'{timestamp} - {msg}' + '\n')

def print_log_in_console():
    with open(log_file, 'r') as f :
        print(f.read())