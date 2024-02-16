# 2.Write a program to implement DFS.

def dfs(graph, start, visited):
    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# graph1 = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
# graph3 = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D'],
#     'C': ['A', 'E', 'F'],
#     'D': ['B'],
#     'E': ['C'],
#     'F': ['C']
# }

start= 'A'
visited = set()

print("DFS Traversal:")
dfs(graph, start, visited)
