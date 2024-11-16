def valor_mais_alto(lista):
  # Caso base: se a lista estiver vazia, retorna o valor mínimo possível (por exemplo, 0 ou -infinito)
    if not lista:
        return float('-inf')  # Retorna o valor mais baixo possível
    
    # Caso recursivo: compara o primeiro item com o maior valor da sublista restante
    primeiro_item = lista[0]
    maior_restante = valor_mais_alto(lista[1:])
    
    # Retorna o maior valor entre o primeiro item e o maior valor da sublista
    return max(primeiro_item, maior_restante)

# Exemplo de uso
lista = [3, 7, 2, 9, 5]
resultado = valor_mais_alto(lista)
print(f"O valor mais alto na lista é: {resultado}")