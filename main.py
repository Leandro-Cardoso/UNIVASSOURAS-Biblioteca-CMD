from screen import draw_screen
from choice import make_choice

# MENU:
from menu.exit import exit
from menu.create_account import create_account
from menu.login import login
from menu.profile import profile
from menu.book_menu import book_menu
from menu.reservations import reservations
from menu.manage_books import manage_books
from menu.manage_users import manage_users

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
            infos = f'bem vindo(a) {username}. selecione uma das opções de serviços abaixo'
            options.extend([
                'relogar',
                'perfil',
                'buscar livro',
                'minhas reservas'
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
        elif choiced == 2:
            user = create_account()
        elif choiced == 3:
            user = login()
        elif choiced == 4:
            user = profile(user)
        elif choiced == 5:
            result = book_menu(user)
            if not isinstance(result, dict):
                erro = result
        elif choiced == 6:
            reservations(user)
        elif choiced == 7:
            user = manage_books(user)
        elif choiced == 8:
            user = manage_users(user)

if __name__ == '__main__':
    main()
