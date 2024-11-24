import heapq

graph = {
    'A': {'B': 5, 'C': 2},
     'B': {'E': 2, 'D': 4},
     'C': {'E': 7},
     'D': {'E': 6, 'F': 3},
     'E': {'F': 1},
     'F': {}
}

def dijkstra(graph, start):
    # Dicionário para armazenar as distâncias mínimas
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0 # Distância até o vértice inicial é 0
    
    # Dicionário para armazenar o camino anterior
    previous_vertices = {vertex: None for vertex in graph}
    
    # Usando uma fila de prioridade (min-heap) para explorar os vértices
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Se a distancia atual for maior que a registrada, ignoramos
        if current_distance > distances[current_vertex]:
            continue
        
        # Explorar os vizinhos do vértice atual
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Se encontrarmos um caminho curto, atualizamos
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances, previous_vertices

start_vertex = 'A'
distances, previous_vertices = dijkstra(graph, start_vertex)

print(f"Distâncias mínimas partindo de {start_vertex}:")

for vertex, distance in distances.items():
    print(f"{start_vertex} => {vertex} = {distance}")
    
print("\nCaminhos mais curtos:")
for vertex, previous in previous_vertices.items():
    path = []
    current = vertex
    while current is not None:
        path.append(current)
        current = previous_vertices[current]
    path.reverse()
    print(f"{start_vertex} => {vertex}: {'=>'.join(path)}")