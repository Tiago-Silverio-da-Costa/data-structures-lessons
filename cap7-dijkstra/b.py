import heapq

# Definição do grafo
graph = {}
graph['a'] = {}
graph['a']['b'] = 10
graph['b'] = {}
graph['b']['d'] = 20
graph['c'] = {}
graph['c']['b'] = 1
graph['c']['d'] = 1
graph['d'] = {}
graph['d']['e'] = 30
graph['e'] = {} 

def dijkstra(graph, start, target):
    # Inicialização das distâncias e da fila de prioridade
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    previous_nodes = {node: None for node in graph}
    
    while priority_queue:
        # Extração do nó com a menor distância
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Caso já tenha encontrado o destino
        if current_node == target:
            break
        
        # Se a distância atual form maior, ignorar (já foi atualizado)
        if current_distance > distances[current_node]:
            continue
        
        # Iterara pelos vizinhos
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Atualizar a distância mínimia encontrada
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
                
    # Reconstruir o caminho a partir do destino
    
    path = []
    current = target
    
    while current:
        path.insert(0, current)
        current = previous_nodes[current]
        
    return distances[target], path

# Uso do algoritmo
start_node = 'a'
end_node = 'e'
shortest_distance, shortest_path = dijkstra(graph, start_node, end_node)

print(f"Menor distância de {start_node} até {end_node}: {shortest_distance}")
print(f"Caminho mais curto: {' -> '.join(shortest_path)}")
    