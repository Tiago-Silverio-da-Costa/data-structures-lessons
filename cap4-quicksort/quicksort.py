def quicksort(array):
    # Caso base: se a lista tiver 0 ou 1 elemento, ela já está ordenada
    if len(array) < 2:
        return array
    else:
        # Escolhe o primeiro elemento como pivô
        pivo = array[0]
        
        # Cria uma lista com todos os elementos menores ou iguais ao pivô
        menores = [i for i in array[1:] if i <= pivo]
        
        # Cria uma lista com todos os elementos maiores que o pivô
        maiores = [i for i in array[1:] if i > pivo]
        
        # Debug: imprime a combinação atual de menores, pivô e maiores
        print(f"Menores: {menores}, Pivô: {pivo}, Maiores: {maiores}")
        
        # Combina recursivamente as sublistas ordenadas (menores + pivô + maiores)
        return quicksort(menores) + [pivo] + quicksort(maiores)

# Teste do algoritmo com uma lista de exemplo
quicksort([10, 5, 2, 3, 8, 7])
