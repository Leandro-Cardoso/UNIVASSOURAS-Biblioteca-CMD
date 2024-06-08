from getpass import getpass

from screen import draw_screen
from choice import make_choice
from user import remove_user, get_user, add_user
from log import log, log_erro

def change_username(user:dict) -> dict:
    # SCREEN:
    title = 'mudar usuário'
    infos = 'digite seu o seu novo nome de usuário'
    erro = None
    options = None
    while True:
        draw_screen(title, infos, options, erro)
        # USERNAME:
        username = input('\n NOVO USUÁRIO: ')
        registered_user = get_user(username)
        if len(username) < 3:
            erro = f'o usuário "{username}" não pode ter menos de 3 caracteres'
            log_erro(erro)
        elif not username.isalnum():
            erro = f'o usuário "{username}" precisa conter apenas letras e números'
            log_erro(erro)
        elif username == user['username']:
            erro = f'o nome de usuário "{username}" já está definido'
            log_erro(erro)
        elif isinstance(registered_user, dict):
            erro = f'já existe usuário "{username}" registrado'
            log_erro(erro)
        else:
            erro = None
            break
    # SET:
    remove_user(user)
    key = 'username'
    user[key] = username
    add_user(user)
    log('nome do usuário alterado', username)
    return user

def change_password(user:dict) -> dict:
    # SCREEN:
    title = 'mudar senha'
    infos = 'digite sua nova senha de usuário'
    erro = None
    options = None
    while True:
        draw_screen(title, infos, options, erro)
        # PASSWORD:
        username = user['username']
        password = getpass('\n NOVA SENHA: ')
        if len(password) < 6:
            erro = f'a senha do usuário "{username}" não pode ter menos de 6 caracteres'
            log_erro(erro)
        else:
            # PASSWORD CONFIRMATION:
            password2 = getpass('\n REPITA A NOVA SENHA: ')
            if password2 == password:
                break
            else:
                erro = f'a senha do usuário "{username}" não foi confirmada'
                log_erro(erro)
    # SET:
    key = 'password'
    user[key] = password
    add_user(user)
    log('senha do usuário alterada', username)
    return user

def profile(user:dict) -> dict:
    # SCREEN:
    title = f'perfil'
    infos = None
    erro = None
    options = [
        'voltar',
        'deslogar',
        'apagar conta',
        'mudar usuário',
        'mudar senha'
    ]
    while True:
        draw_screen(title, infos, options, erro, user)
        # CHOICE:
        choiced = make_choice(options, user['username'])
        # ERRO:
        if isinstance(choiced, str):
            erro = choiced
        else:
            erro = None
        # OPTIONS:
        if choiced == 1:
            break
        elif choiced == 2:
            user = None
            break
        elif choiced == 3:
            remove_user(user)
            user = None
            break
        elif choiced == 4:
            user = change_username(user)
        elif choiced == 5:
            change_password(user)
    return user
