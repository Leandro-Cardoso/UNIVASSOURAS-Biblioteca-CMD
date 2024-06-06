import os
import textwrap

def draw_title(title:str, screen_width:int) -> None:
    h = '|'
    s = ':'
    if title is not str:
        title = str(title)
    title = title.upper()
    title = f'{h} {title} {h}'
    title = f'\n{title:{s}^{screen_width}}'
    print(title)

def draw_infos(infos:str, screen_width:int) -> None:
    sentences = infos.split('.')
    infos = ''
    for sentence in sentences:
        if sentence != '':
            words = sentence.split(' ')
            words[0] = words[0].capitalize()
            sentence = ' '.join(words)
            sentence = f'\t{sentence}.'
            sentence = textwrap.fill(sentence, width = screen_width, subsequent_indent = ' ')
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
        button = f'{d} {i:>2} {d} {option:^{option_width}} {d}'
        menu += f'\n{button:^{screen_width}}'
        menu += bar
    print(menu)

def draw_erro(erro:str, screen_width:int) -> None:
    b = '-'
    if not erro.endswith('.'):
        erro += '.'
    erro = erro.capitalize()
    erro = f' [ERRO] -> {erro} '
    erro = f'\n{erro:{b}^{screen_width}}'
    print(erro)

def draw_screen(title:str, infos:str = None, options:str = None, erro:str = None, width:int = 100):
    os.system('cls')
    draw_title(title, width)
    if infos:
        draw_infos(infos, width)
    if options:
        draw_menu(options, width)
    if erro:
        draw_erro(erro, width)

if __name__ == '__main__':
    title = 'menu'
    infos = 'essa é uma descrição inicial para o assunto abordado aquidasdnal sand ad nasdand çasdn açsd nas da sjnasjd alj da d asd a sldajh a sdhalsjd Alsd ja. Sdadubha sa dajsnda shd bfsdhfb shdfb s fhbsdfh basdfhba s dhfbasfhd bdasf basdfh basdf hbasdfh baskdhf bsdfh bsdkf bskdf hbaksd fhbakfh basdhfb asjdf hbaskdjh fbaskdjfh basdf hbsakdf hbasdfhbdsaj.'
    options = [
        'logar',
        'criar',
        'sair'
    ]
    erro = 'deu pau aqui'
    draw_screen(title, infos, options, erro)
