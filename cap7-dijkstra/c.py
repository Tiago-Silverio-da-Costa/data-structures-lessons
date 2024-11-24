import heapq

graph = {}
graph['a'] = {}
graph['a']['b'] = 2
graph['a']['c'] = 2
graph['c'] = {}
graph['c']['b'] = 2 
graph['b'] = {}
graph['b']['e'] = 2
graph['b']['d'] = 2
graph['d'] = {}
graph['d']['e'] = 2
graph['d']['c'] = -1
graph['e'] = {}

def dijkstra(graph, start, target):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0,start)]
    previous_nodes = {node: None for node in graph}
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_node == target:
            break
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
                
    path = []
    current = target
    
    while current:
        path.insert(0, current)
        current = previous_nodes[current]
        
    return distances[target], path

start_node = 'a'
end_node = 'e'
shortest_distance,shortest_path = dijkstra(graph, start_node, end_node)

print(f"Menor distância de {start_node} até {end_node}: {shortest_distance}")
print(f"Caminho mais curto: {' -> '.join(shortest_path)}")