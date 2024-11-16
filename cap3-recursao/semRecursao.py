def procure_pela_box(caixa_principal):
    pilha = caixa_principal.crie_uma_pilha_para_busca()
    vazia = ""
    while pilha is not vazia:
        caixa = pilha.pegue_caixa()
        for item in caixa:
            if item.e_uma_caixa():
                if item.e_uma_caixa():
                    pilha.append(item)
                elif item.e_uma_chave():
                    print("achei a chave!")
