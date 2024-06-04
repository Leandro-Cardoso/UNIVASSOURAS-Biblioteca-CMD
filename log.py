from datetime import datetime
from os import path

raiz = 'logs'
extensao = 'txt'

def salvar_log(mensagem:str) -> None:
    '''Salva o log em um arquivo TXT.'''
    mensagem = mensagem.capitalize()
    if not mensagem.endswith('.'):
        mensagem += '.'
    agora = datetime.now()
    data = agora.strftime('%Y-%m-%d')
    tempo = agora.strftime('%H : %M : %S')
    nome_arquivo = data + '.' + extensao
    caminho_arquivo = path.join(path.basename(raiz), path.basename(nome_arquivo))
    with open(caminho_arquivo, 'a', encoding = 'UTF-8') as file:
        file.write(f'{tempo} -> {mensagem}\n')
