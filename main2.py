from screen import draw_screen
from choice import make_choice
from log import log

def exit(username:str) -> None:
    title = 'biblioteca'
    infos = f'obrigado {username} por utilizar nosso sistema. volte sempre'
    draw_screen(title, infos)
    print()

def login(user:dict) -> dict:
    pass

def main_menu(user:dict) -> None:
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
            options.append(
                'editar conta',
                'minhas reservas',
                'buscar livro'
            )
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
            choiced, erro = make_choice(options, username)
        else:
            choiced, erro = make_choice(options)
        if choiced == 1:
            log('saiu do sistema', username)
            exit(username)
            break

def main() -> None:
    user = None
    main_menu(user)

if __name__ == '__main__':
    main()
