from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = [] 
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

def pessoa_e_vendedor(nome):
    return nome[-1] == 'm'

def pesquisa(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += graph[nome]
    verificados = []
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificados:
            if pessoa_e_vendedor(pessoa):
                print(pessoa + " é um vendendor de manga!")
                return True
            else:
                fila_de_pesquisa += graph[pessoa]
                verificados.append(pessoa)
    return False

pesquisa('you')

