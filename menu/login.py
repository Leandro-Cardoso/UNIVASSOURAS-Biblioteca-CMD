from screen import draw_screen
from user import get_user
from log import log, log_erro

def login() -> dict:
    # SCREEN:
    title = 'login'
    infos = 'digite seu o seu nome de usuário e sua senha'
    erro = None
    options = None
    while True:
        draw_screen(title, infos, options, erro)
        # USERNAME:
        username = input('\nUSUÁRIO: ')
        user = get_user(username)
        if isinstance(user, str):
            erro = user
            log_erro(erro)
        else:
            erro = None
            break
    while True:
        draw_screen(title, infos, options, erro)
        # PASSWORD:
        password = input('\nSENHA: ')
        if password != user['password']:
            erro = f'a senha está incorreta'
            log_erro(erro, user['name'])
        else:
            break
    log('entrou no sistema', username)
    return user
