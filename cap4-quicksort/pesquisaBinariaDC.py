def pesquisa_binaria(lista, item, esquerda=0, direita=None):
    if direita is None:
        direita = len(lista) - 1
    
    # Caso base 1: O item foi encontrado
    if esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == item:
            return meio  # Item encontrado, retorna o índice
        
        # Caso base 2: Intervalo de pesquisa vazio (item não encontrado)
        elif lista[meio] < item:
            return pesquisa_binaria(lista, item, meio + 1, direita)  # Busca na metade direita
        else:
            return pesquisa_binaria(lista, item, esquerda, meio - 1)  # Busca na metade esquerda
    else:
        return -1  # Item não encontrado, retorna -1

# Exemplo de uso:
lista = [1, 3, 5, 7, 9, 11, 13, 15]
item = 9
resultado = pesquisa_binaria(lista, item)
if resultado != -1:
    print(f"Item encontrado no índice: {resultado}")
else:
    print("Item não encontrado.")
