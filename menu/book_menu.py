from screen import draw_screen
from book import get_book, add_book, remove_book
from log import log_erro, log
from choice import make_choice
from user import add_user

def search_book(user:dict) -> dict|str:
    username= user['username']
    # SCREEN:
    title = 'buscar livro'
    infos = 'digite o titulo do livro que busca'
    draw_screen(title, infos)
    # TITLE:
    booktitle = input('\n LIVRO: ')
    book = get_book(booktitle)
    if isinstance(book, str):
        log_erro(book, username)
    else:
        log(f'buscou o livro "{booktitle}"', username)
    return book

def book_menu(user:dict) -> str:
    username= user['username']
    # SEARCH:
    book = search_book(user)
    if isinstance(book, str):
        return book
    # SCREEN:
    title = 'livro'
    erro = None
    while True:
        options = [
            'voltar',
            'nova busca'
        ]
        titles = []
        books = list(user['books'])
        for dictionary in books:
            titles.append(dictionary['title'])
        if not book['title'] in titles:
            options.append(
                'reservar'
            )
        draw_screen(title, options = options, erro = erro, dictionary = book)
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
            result = search_book(user)
            if isinstance(result, dict):
                book = result
                erro = None
            else:
                erro = book
        elif choiced == 3:
            book['quantity'] -= 1
            if book['quantity'] <= 0:
                remove_book(book)
                book['quantity'] = 1
                if user['books']:
                    user['books'] = list(user['books']).append(book)
                else:
                    user['books'] = [book]
                add_user(user)
                log(f'o livro {book['title']} foi reservado', username)
                break
            else:
                add_book(book)
                book['quantity'] = 1
                if user['books']:
                    user['books'] = list(user['books']).append(book)
                else:
                    user['books'] = [book]
                add_user(user)
                log(f'o livro {book['title']} foi reservado', username)
