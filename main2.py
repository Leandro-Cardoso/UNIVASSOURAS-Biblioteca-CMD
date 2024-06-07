from screen import draw_screen
from choice import make_choice
from log import log

from menu.exit import exit
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
            'logar'
        ]
        if user:
            username = user['name']
            infos = f'bem vindo {username}. selecione uma das opções de serviços abaixo'
            options.extend([
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
                'criar conta'
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
            log('saiu do sistema', username)
            exit(username)
            break
        if choiced == 2:
            user = login()

if __name__ == '__main__':
    main()
