from screen import draw_screen
from choice import make_choice

def manage_books(user:dict) -> dict:
    username = user['username']
    # SCREEN:
    title = 'gerenciar livros'
    infos = 'selecione a opção de gerenciamendo de livros desejada'
    options = [
        'voltar',
        'adicionar livros',
        'remover livros',
        'devolver reserva'
    ]
    erro = None
    while True:
        draw_screen(title, infos, options, erro)
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
        elif choiced == 2:
            pass
        elif choiced == 3:
            pass
        elif choiced == 4:
            pass
    return user
