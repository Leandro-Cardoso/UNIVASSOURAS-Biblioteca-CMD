def buscar_dicionario(dicionario:dict, alvo:str) -> dict:
    '''Buscar um dicionário e retorna-lo.'''
    for chave in list(dicionario):
        if chave == alvo:
            return {chave : dicionario[chave]}
    return {}

def subtrair_dicionarios(dicionario_1:dict, dicionario_2:dict) -> dict:
    '''Subtrai dois dicionários e retorna um novo dicionário.'''
    for chave in list(dicionario_2):
        if chave in list(dicionario_1):
            if type(dicionario_1[chave]) == int or type(dicionario_1[chave]) == float:
                dicionario_1[chave] -= dicionario_2[chave]
                if dicionario_1[chave] <= 0:
                    del dicionario_1[chave]
            else:
                del dicionario_1[chave]
    return dicionario_1

def somar_dicionarios(dicionario_1:dict, dicionario_2:dict) -> dict:
    '''Soma dois dicionários e retorna um novo dicionário.'''
    for chave in list(dicionario_2):
        if chave in list(dicionario_1):
            dicionario_1[chave] += dicionario_2[chave]
        else:
            dicionario_1.update({chave : dicionario_2[chave]})
    return dicionario_1
