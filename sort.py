def merge(lista:list, inicio:int, meio:int, fim:int) -> list:
    metade_1 = lista[inicio : meio]
    metade_2 = lista[meio : fim]
    topo_1 = 0
    topo_2 = 0
    for i in range(inicio, fim):
        if topo_1 >= len(metade_1):
            lista[i] = metade_2[topo_2]
            topo_2 += 1
        elif topo_2 >= len(metade_2):
            lista[i] = metade_1[topo_1]
            topo_1 += 1
        elif metade_1[topo_1] < metade_2[topo_2]:
            lista[i] = metade_1[topo_1]
            topo_1 += 1
        else:
            lista[i] = metade_2[topo_2]
            topo_2 += 1

def merge_sort(lista:list, inicio:int = 0, fim:int = None) -> list:
    '''Algoritmo "Merge Sort" para ordenar uma lista de forma eficiente.'''
    if fim is None:
        fim = len(lista)
    if fim - inicio > 1:
        meio = (fim + inicio) // 2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio, fim)
        merge(lista, inicio, meio, fim)
    return lista
