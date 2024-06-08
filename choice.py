from log import log, log_erro

def make_choice(options:list, username:str = '') -> int|str:
    choiced = input('\n OPÇÃO: ')
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
        erro = f'opção {choiced} é inválida'
        log_erro(erro, username)
        return erro
