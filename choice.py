from log import log, log_erro

def make_choice(options:list, username:str = '') -> int:
    choiced = input('OPÇÃO: ')
    try:
        choiced = int(choiced)
        n = len(options)
        if 0 < choiced <= n:
            option = str(options[choiced - 1]).title()
            log(f'acessou a opção {choiced} - {option}', username)
            return choiced
        else:
            raise
    except:
        log_erro(f'opção {choiced} é inválida', username)
        return -1

if __name__ == '__main__':
    options = [
        'sair',
        'avançar'
    ]
    username = 'Leandro'
    make_choice(options, username)
