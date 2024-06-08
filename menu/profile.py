from screen import draw_screen
from choice import make_choice
from user import remove_user

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
    return user
