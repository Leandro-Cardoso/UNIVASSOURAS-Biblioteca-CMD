from datetime import datetime
from os import path

from config import RAIZ_LOG, EXTENSAO_LOG

def salvar_log(mensagem:str) -> None:
    '''Salva o log em um arquivo TXT.'''
    mensagem = mensagem.capitalize()
    if not mensagem.endswith('.'):
        mensagem += '.'
    agora = datetime.now()
    data = agora.strftime('%Y-%m-%d')
    tempo = agora.strftime('%H : %M : %S')
    nome_arquivo = data + '.' + EXTENSAO_LOG
    caminho_arquivo = path.join(path.basename(RAIZ_LOG), path.basename(nome_arquivo))
    with open(caminho_arquivo, 'a', encoding = 'UTF-8') as file:
        file.write(f'{tempo} -> {mensagem}\n')
