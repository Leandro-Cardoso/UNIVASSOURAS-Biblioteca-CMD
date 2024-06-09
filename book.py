from os import path, remove, listdir
from json import dumps, loads

from config import BOOK_EXTEXSION, BOOK_ROOT
from log import log_erro

def get_bookpath(title:str) -> str:
    filename = f'{title}.{BOOK_EXTEXSION}'
    filename = filename.replace(' ', '_')
    filepath = path.join(path.basename(BOOK_ROOT), path.basename(filename))
    return filepath

def add_book(book:dict) -> None:
    title = book['title']
    bookpath = get_bookpath(title)
    book = str(dumps(book))
    try:
        with open(bookpath, 'w', encoding = 'UTF-8') as file:
            file.write(book)
    except:
        log_erro(f'a pasta raiz "{BOOK_ROOT}" não foi encontrada')

def remove_book(book:dict) -> None:
    title = book['title']
    bookpath = get_bookpath(title)
    try:
        remove(bookpath)
    except:
        log_erro(f'o livro "{title}" não foi encontrado')

def get_book(title:str) -> dict|str:
    bookpath = get_bookpath(title)
    try:
        with open(bookpath, 'r', encoding = 'UTF-8') as file:
            content = file.read()
        book = loads(content)
        return book
    except:
        erro = f'o livro "{title}" não foi encontrado'
        return erro

def list_books(dir:str = BOOK_ROOT, ext:str = BOOK_EXTEXSION) -> list:
    ext = f'.{ext}'
    files = listdir(dir)
    titles = []
    for filename in files:
        if filename.endswith(ext):
            title = filename.replace(ext, '')
            title = title.replace('_', ' ')
            titles.append(title)
    return titles
