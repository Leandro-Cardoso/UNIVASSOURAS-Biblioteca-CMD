from screen import draw_screen
from choice import make_choice
from book import get_book, add_book
from log import log, log_erro

def add_books(user:dict) -> None:
    username = user['username']
    # SCREEN:
    title = 'adicionar livros'
    infos = 'digite as informações abaixo pedidas e necessárias para adicionar um novo livro ou adicionar mais unidades'
    erro = None
    # TITLE:
    draw_screen(title, infos, erro = erro)
    booktitle = input('\n LIVRO: ')
    booktitle = booktitle.title()
    book = get_book(booktitle)
    if isinstance(book, dict):
        while True:
            draw_screen(title, infos, erro = erro, dictionarys = book)
            quantity = input('\n QUANTIDADE: ')
            if quantity.isnumeric():
                quantity = int(quantity)
                if quantity > 0:
                    book['quantity'] += quantity
                    break
                else:
                    erro = f'a quantidade "{quantity}" precisa ser maior que 0'
                    log_erro(erro, username)
            else:
                erro = f'a quantidade "{quantity}" não é um número inteiro'
                log_erro(erro, username)
    else:
        book = {}
        book['title'] = booktitle
        draw_screen(title, infos, erro = erro)
        author = input('\n AUTOR: ')
        author = author.title()
        book['author'] = author
        while True:
            draw_screen(title, infos, erro = erro)
            quantity = input('\n QUANTIDADE: ')
            if quantity.isnumeric():
                quantity = int(quantity)
                if quantity > 0:
                    break
                else:
                    erro = f'a quantidade "{quantity}" precisa ser maior que 0'
                    log_erro(erro, username)
            else:
                erro = f'a quantidade "{quantity}" não é um número inteiro'
                log_erro(erro, username)
        book['quantity'] = quantity
    # SET:
    add_book(book)
    log(f'o livro "{booktitle}" foi adicionado', username)

def remove_books(user:dict) -> None:
    # SCREEN:
    title = 'remover livros'
    infos = 'digite o titulo do livro e a quantidade para remover do acervo de livros'
    erro = None
    book = None
    while True:
        draw_screen(title, infos, erro = erro, dictionarys = book)
        # BOOK:
        booktitle = input('\n LIVRO: ')
        book = get_book(booktitle)
        break

def return_reserved_book(user:dict) -> dict:
    # SCREEN:
    title = 'devolver livro reservado'
    infos = 'digite o nome do usuário e o titulo do livro para realizar a devolução ao acervo de livros'
    erro = None
    while True:
        draw_screen(title, infos, erro = erro)
        break
    return user

def list_books(user:dict) -> None:
    title = 'listar livros'
    options = [
        ''
    ]
    erro = None
    books = None
    while True:
        draw_screen(title, options = options, erro = erro, dictionarys = books)
        break

def manage_books(user:dict) -> dict:
    username = user['username']
    # SCREEN:
    title = 'gerenciar livros'
    infos = 'selecione a opção de gerenciamendo de livros desejada'
    options = [
        'voltar',
        'adicionar livros',
        'remover livros',
        'devolver livro reservado',
        'listar livros'
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
            add_books(user)
        elif choiced == 3:
            remove_books(user)
        elif choiced == 4:
            user = return_reserved_book(user)
        elif choiced == 5:
            list_books(user)
    return user
