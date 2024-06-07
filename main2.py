from screen import draw_screen
from choice import make_choice

def login(user:dict) -> dict:
    pass

def main_menu(user:dict) -> None:
    title = 'menu principal'
    options = [
        'sair',
        'logar'
        ]
    while True:
        if user:
            infos = f'bem vindo {user}. selecione uma das opções de serviços abaixo'
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
        draw_screen(title, infos, options)
        if user:
            make_choice(options, user['name'])
        else:
            make_choice(options)

def main() -> None:
    user = None
    main_menu(user)

if __name__ == '__main__':
    main()
