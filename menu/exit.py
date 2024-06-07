from screen import draw_screen

def exit(username:str) -> None:
    # SCREEN:
    title = 'biblioteca'
    infos = f'obrigado {username} por utilizar nosso sistema. volte sempre'
    draw_screen(title, infos)
    print()
