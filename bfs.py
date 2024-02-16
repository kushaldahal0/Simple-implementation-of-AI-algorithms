from queue import Queue
graph ={
    'A': ['B','C'],
    'B': ['D','C'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F':[]
}

def bfs(graph, start, goal):
    visited = set()
    q = Queue()
    q.put(start)
    while not q.empty():
        node = q.get()
        if goal not in visited:
            if node not in visited:
                visited.add(node)
                print(node)

                for neighbor in graph(node):
                    q.put(neighbor)

bfs(graph, 'A','E')