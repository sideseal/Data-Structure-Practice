# BFS, DFS

from queue import Queue

def bfs(graph, start_node):
    visit = {}
    queue = Queue()

    queue.put(start_node)

    while queue.qsize() > 0:
        node = queue.get()
        if node not in visit:
            visit[node] = True
            for nextNode in graph[node]:
                queue.put(nextNode)
    
    return list(visit.keys())

def dfs(graph, start_node):
    visit = {}
    stack = []

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit[node] = True
            stack.extend(graph[node])

    return list(visit.keys())

if __name__ == "__main__":
    graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D'],
        'D': ['C', 'E', 'G'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }

    print(bfs(graph, 'A'))
    print(dfs(graph, 'A'))