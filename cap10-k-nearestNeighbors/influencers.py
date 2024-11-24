avaliacoes = {
        "Tarantino": {"Filme A": 5, "Filme B": 4},
    "Wes Anderson": {"Filme A": 4, "Filme B": 5},
    "Usuário Comum": {"Filme A": 3, "Filme B": 2},
}

pesos = {"Tarantino": 2, "Wes Anderson": 2, "Usuário Comum": 1}

def media_ponderada(filme, avaliacoes, pesos):
    total_peso = 0
    soma = 0
    for usuario, notas in avaliacoes.items():
        if filme in notas:
            soma += notas[filme] * pesos[usuario]
            total_peso += pesos[usuario]
    return soma / total_peso if total_peso != 0 else 0

print("Nota ponderada para Filme A:", media_ponderada("Filme A", avaliacoes, pesos))
print("Nota ponderada para Filme B:", media_ponderada("Filme B", avaliacoes, pesos))