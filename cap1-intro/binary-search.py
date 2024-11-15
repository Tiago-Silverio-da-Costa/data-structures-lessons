def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        print("pega adivinhações e máx de passos", meio)
        if chute == item:
            print("resposta:", meio)
            return meio + 1
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None
    
minha_lista = list(range(1, 450))


print(pesquisa_binaria(minha_lista, 338))
