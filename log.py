from datetime import datetime
from os import path, makedirs

from config import LOG_ROOT, LOG_EXTENSION

def log(text:str, username:str = '') -> None:
    '''Salva o log em um arquivo TXT.'''
    username = username.title()
    words = text.split(' ')
    if '[ERRO]' in words:
        i = 1
    else:
        i = 0
    words[i] = words[i].capitalize()
    text = ' '.join(words)
    if not text.endswith('.'):
        text += '.'
    now = datetime.now()
    date = now.strftime('%Y-%m-%d')
    time = now.strftime('%H:%M:%S')
    filename = date + '.' + LOG_EXTENSION
    filepath = path.join(path.basename(LOG_ROOT), path.basename(filename))
    # Check root:
    if not path.exists(LOG_ROOT):
        makedirs(LOG_ROOT)
    # Save file:
    with open(filepath, 'a', encoding = 'UTF-8') as file:
        file.write(f'{time} ({username}) -> {text}\n')

def log_erro(text:str, username:str = '') -> None:
    '''Salva o log de erro em um arquivo TXT.'''
    text = f'[ERRO] {text}'
    log(text, username)
