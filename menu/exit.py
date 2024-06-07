from screen import draw_screen
from log import log

def exit(username:str) -> None:
    # SCREEN:
    title = 'biblioteca'
    infos = f'obrigado {username} por utilizar nosso sistema. volte sempre'
    draw_screen(title, infos)
    log('saiu do sistema', username)
