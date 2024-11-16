# essa função vai busca o menor número em um array
def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0
    
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
            print("menor", menor)
            print("menor_indice", menor_indice)
    return menor_indice

# essa função cria um novo array, para armazenar em order crescente
def ordenacaoporSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
        print("novoArr", novoArr)
    return novoArr

print(ordenacaoporSelecao([5, 3, 6, 2, 10]))