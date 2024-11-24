# Importação do heapq não é necessária para este algoritmo

# Definição das estações e estados cobertos por elas
estacoes = {}
estacoes['kum'] = set(['id', 'nv', 'ut'])
estacoes['kdois'] = set(['wa', 'id', 'mt'])
estacoes['ktres'] = set(['or', 'nv', 'ca'])
estacoes['kquatro'] = set(['nv', 'ut'])
estacoes['kcinco'] = set(['ca', 'az'])

# Definir os estados que precisamos cobrir
estados_abranger = set(['wa', 'id', 'mt', 'nv', 'ut', 'ca', 'az', 'or'])

# Conjunto final de estações escolhidas
estacoes_final = set()

# Enquanto existirem estados a serem cobertos
while estados_abranger:
    melhor_estacao = None
    estados_cobertos = set()

    # Encontrar a melhor estação que cobre o maior número de estados restantes
    for estacao, estados_por_estacao in estacoes.items():
        cobertos = estados_abranger & estados_por_estacao
        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = cobertos

    # Adicionar a melhor estação ao conjunto final e remover os estados cobertos
    if melhor_estacao:
        estacoes_final.add(melhor_estacao)
        estados_abranger -= estados_cobertos

# Exibir o resultado
print(f"Estações escolhidas: {estacoes_final}")
                                