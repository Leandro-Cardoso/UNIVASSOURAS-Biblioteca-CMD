from screen import draw_screen
from choice import make_choice

def reservations(user:dict) -> None:
    username = user['username']
    # SCREEN:
    title = 'minhas reservas'
    options = [
        'voltar'
    ]
    erro = None
    dictionarys = user['books']
    while True:
        draw_screen(title, options = options, erro = erro, dictionarys = dictionarys)
        # CHOICE:
        choiced = make_choice(options, username)
        # ERRO:
        if isinstance(choiced, str):
            erro = choiced
        else:
            erro = None
        # OPTIONS:
        if choiced == 1:
            break
