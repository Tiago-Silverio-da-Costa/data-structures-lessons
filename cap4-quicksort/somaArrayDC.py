def soma_array(arr):
    # Caso base: se o array tem apenas um elemento, retorne esse elemento
    if len(arr) == 1:
        return arr[0]
    
    # Dividir o array ao meio
    meio = len(arr) // 2
    esquerda = arr[:meio] # Primeira metade
    direita = arr[meio:] # Segunda metade
    
    # Conquistar: somar as duas metades recursivamente
    soma_esquerda = soma_array(esquerda)
    soma_direita = soma_array(direita)
    
    # Combinar: somar as somas das metades
    return soma_esquerda + soma_direita

arr = [1, 2, 3, 4, 5, 6, 7, 8]
resultado = soma_array(arr)
print(f"Soma dos elementos do array: {resultado}")