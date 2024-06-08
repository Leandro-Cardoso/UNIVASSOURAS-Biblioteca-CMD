import os
import textwrap

def draw_title(title:str, screen_width:int) -> None:
    h = '|'
    s = ':'
    title = title.upper()
    title = f'{h} {title} {h}'
    title = f'\n{title:{s}^{screen_width}}'
    print(title)

def draw_infos(infos:str, screen_width:int) -> None:
    sentences = infos.split('.')
    infos = ''
    for sentence in sentences:
        if sentence != '':
            if sentence.startswith(' '):
                sentence = sentence[1:]
            words = sentence.split(' ')
            words[0] = words[0].capitalize()
            sentence = ' '.join(words)
            sentence = f'\t{sentence}.'
            sentence = textwrap.fill(sentence, width = screen_width)
            infos += f'\n{sentence}'
    print(infos)

def draw_menu(options:list, screen_width:int) -> None:
    b = '-'
    d = '|'
    longest_option = max(options, key=len)
    option_width = len(longest_option)
    bar = b * (option_width + 9)
    bar = f'\n{bar:^{screen_width}}'
    menu = bar
    for i, option in enumerate(options):
        option = str(option).title()
        button = f'{d} {(i + 1):>2} {d} {option:<{option_width}} {d}'
        menu += f'\n{button:^{screen_width}}'
        menu += bar
    print(menu)

def draw_erro(erro:str, screen_width:int) -> None:
    b = '-'
    if not erro.endswith('.'):
        erro += '.'
    words = erro.split(' ')
    words[0] = words[0].capitalize()
    erro = ' '.join(words)
    erro = f' [ERRO] -> {erro} '
    erro = f'\n{erro:{b}^{screen_width}}'
    print(erro)

def draw_dict(dictionary:dict, screen_width:int, ignore:list = ['password', 'senha']) -> None:
    b = '-'
    bar = b * screen_width
    text = ''
    for key in dictionary.keys():
        if not key in ignore:
            value = dictionary[key]
            key = str(key).title()
            text += f'\n{key:>{screen_width // 2}} : {value}'
    text = f'\n{text}\n\n{bar}'
    print(text)

def draw_dicts(dictionarys:list, screen_width:int, ignore:list = ['password', 'senha']) -> None:
    for dictionary in dictionarys:
        draw_dict(dictionary, screen_width, ignore)

def draw_screen(title:str, infos:str = None, options:str = None, erro:str = None, dictionarys:dict|list = None, width:int = 100):
    os.system('cls')
    draw_title(title, width)
    if infos:
        draw_infos(infos, width)
    if dictionarys:
        if isinstance(dictionarys, dict):
            dictionarys = [dictionarys]
        draw_dicts(dictionarys, width)
    if options:
        draw_menu(options, width)
    if erro:
        draw_erro(erro, width)
