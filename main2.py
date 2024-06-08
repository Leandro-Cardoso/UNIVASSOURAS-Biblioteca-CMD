from screen import draw_screen
from choice import make_choice
# MENU:
from menu.exit import exit
from menu.create_account import create_account
from menu.login import login

def main() -> None:
    user = None
    # SCREEN:
    title = 'menu principal'
    username = ''
    erro = None
    while True:
        options = [
            'sair',
            'criar conta'
        ]
        if user:
            username = user['username']
            infos = f'bem vindo {username}. selecione uma das opções de serviços abaixo'
            options.extend([
                'relogar',
                'editar conta',
                'minhas reservas',
                'buscar livro'
            ])
            if user['permission'] == 'admin' or user['permission'] == 'librarian':
                options.append(
                    'gerenciar livros'
                )
            if user['permission'] == 'admin':
                options.append(
                    'gerenciar usuários'
                )
        else:
            options.append(
                'logar'
            )
            infos = 'faça o login ou registre-se para ter acesso aos nossos serviços'
        draw_screen(title, infos, options, erro)
        # CHOICE:
        if user:
            choiced = make_choice(options, username)
        else:
            choiced = make_choice(options)
        # ERRO:
        if isinstance(choiced, str):
            erro = choiced
        else:
            erro = None
        # OPTIONS:
        if choiced == 1:
            exit(username)
            break
        if choiced == 2:
            user = create_account()
        if choiced == 3:
            user = login()

if __name__ == '__main__':
    main()
