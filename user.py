from os import path, remove, listdir
from json import loads, dumps

from config import USER_EXTEXSION, USER_ROOT
from log import log_erro

def get_userpath(username:str) -> str:
    filename = f'{username}.{USER_EXTEXSION}'
    filepath = path.join(path.basename(USER_ROOT), path.basename(filename))
    return filepath

def add_user(user:dict) -> None:
    user['username'] = str(user['username']).lower()
    username = user['username']
    filepath = get_userpath(username)
    user = dumps(user)
    user = str(user)
    try:
        with open(filepath, 'w', encoding = 'UTF-8') as file:
            file.write(user)
    except:
        log_erro(f'a pasta raiz "{USER_ROOT}" não foi encontrada')

def remove_user(user:dict) -> None:
    user['username'] = str(user['username']).lower()
    username = user['username']
    filepath = get_userpath(username)
    try:
        remove(filepath)
    except:
        log_erro(f'o usuário "{username}" não foi encontrado')

def get_user(username:str) -> dict|str:
    username = username.lower()
    filepath = get_userpath(username)
    try:
        with open(filepath, 'r', encoding = 'UTF-8') as file:
            content = file.read()
        user = loads(content)
        return user
    except:
        erro = f'o usuário "{username}" não foi encontrado'
        return erro
    
def list_users(dir:str = USER_ROOT, ext:str = USER_EXTEXSION) -> list:
    ext = f'.{ext}'
    files = listdir(dir)
    usernames = []
    for filename in files:
        if filename.endswith(ext):
            username = filename.replace(ext, '')
            username = username.replace('_', ' ')
            usernames.append(username)
    return usernames
