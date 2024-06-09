from screen import draw_screen
from choice import make_choice

def manage_users(user:dict) -> dict:
    username = user['username']
    # SCREEN:
    title = 'gerenciar usuários'
    infos = 'selecione a opção de gerenciamendo de usuários desejada'
    options = [
        'voltar',
        'remover usuário',
        'listar usuários',
        'mudar permissão'
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
