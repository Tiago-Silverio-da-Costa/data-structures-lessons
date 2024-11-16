def contar_itens(lista):
    # Caso base: Se a lista estiver vazia, retorna 0
    if not lista:
        return 0
    
    # Caso recursivo: Conta o primeiro item e chama recursivamente para o resto da lista
    return 1 + contar_itens(lista[1:])
    # contar_itens(lista[1:]): Esta parte é a chamada recursiva. lista[1:] cria uma sublista que contém todos os itens da lista, exceto o primeiro. Em outras palavras, ela remove o primeiro item da lista e passa essa sublista (sem o primeiro item) para a próxima chamada recursiva.

# Exemplo de uso
lista = [10, 20, 30, 40, 50]
resultado = contar_itens(lista)
print(f"Número de itens na lista: {resultado}")
