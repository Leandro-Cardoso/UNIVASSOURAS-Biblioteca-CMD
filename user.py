from os import path, remove
from json import loads, dumps

from config import USER_EXTEXSION, USER_ROOT
from log import log, log_erro

def get_user_filepath(username:str) -> str:
    filename = f'{username}.{USER_EXTEXSION}'
    filepath = path.join(path.basename(USER_ROOT), path.basename(filename))
    return filepath

def add_user(user:dict) -> None:
    username = user['username']
    filepath = get_user_filepath(username)
    user = dumps(user)
    user = str(user)
    try:
        with open(filepath, 'w', encoding = 'UTF-8') as file:
            file.write(user)
        log(f'usuário "{username}" criado')
    except:
        log_erro(f'a pasta raiz "{USER_ROOT}" não foi encontrada')

def remove_user(user:dict) -> None:
    username = user['username']
    filepath = get_user_filepath(username)
    try:
        remove(filepath)
        log(f'usuário "{username}" removido')
    except:
        log_erro(f'o usuário "{username}" não foi encontrado')

def get_user(username:str) -> dict|str:
    filepath = get_user_filepath(username)
    try:
        with open(filepath, 'r', encoding = 'UTF-8') as file:
            content = file.read()
        user = loads(content)
        return user
    except:
        erro = f'o usuário "{username}" não foi encontrado'
        return erro
