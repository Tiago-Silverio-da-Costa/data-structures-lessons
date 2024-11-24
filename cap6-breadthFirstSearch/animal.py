from collections import deque

def bfs_shortest_path(graph, start, goal):
    queue = deque([[start]])
    
    visited = set()
    
    while queue:
        path = queue.popleft()
        
        node = path[-1]

        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            
            for neighbor in graph[node]:
                new_path = path + [neighbor]
                queue.append(new_path)
    return None


graph = {
    'JATO': ['GATO', 'TATO'],
    'GATO': ['JATO', 'TATO', 'GRATO', 'GADO'],
    'TATO': ['JATO','GATO', 'CHATO'],
    'GRATO': ['GATO', 'GADO'],
    'CHATO': ['TATO', 'GADO'],
    'GADO': []
}

start = 'JATO'
goal = 'GADO'
shortest_path = bfs_shortest_path(graph, start, goal)

print("Menor caminho de {} para {}:".format(start, goal), shortest_path)