from os import path, remove
from json import loads, dumps

from config import USER_EXTEXSION, USER_ROOT
from log import log, log_erro

def get_user_filepath(name:str) -> str:
    filename = f'{name}.{USER_EXTEXSION}'
    filepath = path.join(path.basename(USER_ROOT), path.basename(filename))
    return filepath

def add_user(user:dict) -> None:
    name = user['name']
    filepath = get_user_filepath(name)
    user = dumps(user)
    user = str(user)
    try:
        with open(filepath, 'w', encoding = 'UTF-8') as file:
            file.write(user)
        log(f'usuário {name} criado')
    except:
        log_erro(f'a pasta raiz "{USER_ROOT}" não foi encontrada')

def remove_user(user:dict) -> None:
    name = user['name']
    filepath = get_user_filepath(name)
    try:
        remove(filepath)
        log(f'usuário {name} removido')
    except:
        log_erro(f'o usuário {name} não foi encontrado')

def get_user(username:str) -> dict|str:
    filepath = get_user_filepath(username)
    try:
        with open(filepath, 'r', encoding = 'UTF-8') as file:
            content = file.read()
        user = loads(content)
        return user
    except:
        erro = f'o usuário {username} não foi encontrado'
        log_erro(erro)
        return erro

if __name__ == '__main__':
    user = {
        'name' : 'Leandro',
        'password' : '2510',
        'permission' : 'admin'
    }
    add_user(user)
    user_c = get_user('Leandro')
    print(user_c['name'], user_c['permission'])
