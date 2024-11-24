from collections import deque

def bfs_shortest_path(graph, start, goal): 
    # Fila para manter os caminhos a serem explorados
    queue = deque([[start]])
    # Conjunto para manter os vértices visitados
    visited = set()
    
    while queue:
        # Retira o primeiro caminho da fila
        path = queue.popleft()
        # Pega o último nó do caminho atual
        node = path[-1]
        
        # Verifica se é o nó de destino
        if node == goal:
            return path
        
        # Caso ainda não tenha sido visitado
        if node not in visited:
            # Marca como visitado
            visited.add(node)
            # Adiciona todos os vizinhos do nó atual na fila
            for neighbor in graph[node]:
                new_path = path + [neighbor]
                queue.append(new_path)
                
    return None # Retorna None se não houver caminho

# Grafo representado como um dicionário

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['C', 'F'],
    'F': []
}

# Econtrar o menor caminho de A para F
start = 'A'
goal = 'F'
shortest_path = bfs_shortest_path(graph, start, goal)

print("Menor caminho de {} para {}:".format(start, goal), shortest_path)