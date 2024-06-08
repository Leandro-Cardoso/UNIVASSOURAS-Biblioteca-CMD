from getpass import getpass

from screen import draw_screen
from user import get_user, add_user
from log import log, log_erro

def create_account() -> dict:
    # SCREEN:
    title = 'criar conta'
    infos = 'digite seu o seu nome de usuário e sua senha'
    erro = None
    options = None
    while True:
        draw_screen(title, infos, options, erro)
        # USERNAME:
        username = input('\n USUÁRIO: ')
        user = get_user(username)
        if len(username) < 3:
            erro = f'o usuário "{username}" não pode ter menos de 3 caracteres'
            log_erro(erro)
        elif not username.isalnum():
            erro = f'o usuário "{username}" precisa conter apenas letras e números'
            log_erro(erro)
        elif not isinstance(user, str):
            erro = f'o usuário "{username}" já existe'
            log_erro(erro)
        else:
            erro = None
            break
    while True:
        draw_screen(title, infos, options, erro)
        # PASSWORD:
        password = getpass('\n SENHA: ')
        if len(password) < 6:
            erro = f'a senha do usuário "{username}" não pode ter menos de 6 caracteres'
            log_erro(erro)
        else:
            # PASSWORD CONFIRMATION:
            password2 = getpass('\n REPITA A SENHA: ')
            if password2 == password:
                break
            else:
                erro = f'a senha do usuário "{username}" não foi confirmada'
                log_erro(erro)
    # CREATE:
    new_user = {
        'username' : username,
        'password' : password,
        'permission' : None,
        'books' : []
    }
    add_user(new_user)
    log('usuário criado', username)
    log('entrou no sistema', username)
    return new_user
