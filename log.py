from datetime import datetime
from os import path

RAIZ = 'logs'

def salvar_log(mensagem:str) -> None:
    '''Salva o log em um arquivo TXT.'''
    mensagem.capitalize()
    if not mensagem.endswith('.'):
        mensagem += '.'
    agora = datetime.now()
    data = agora.strftime('%Y-%m-%d')
    tempo = agora.strftime('%H : %M : %S')
    nome_arquivo = data + '.txt'
    caminho_arquivo = path.join(path.basename(RAIZ), path.basename(nome_arquivo))
    with open(caminho_arquivo, 'a') as file:
        file.write(f'{tempo} -> {mensagem}\n')
