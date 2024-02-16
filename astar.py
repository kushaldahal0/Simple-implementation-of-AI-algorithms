graph = {
    'A' : {'B':1, 'C':3},
    'B' : {'D':5, 'E':6},
    'C' : {'D' :2},
    'E' : {}
}

hn = {
    'A' : 6,
    'B' : 3,
    'C' : 4,
    'D' : 2,
    'E' : 0
}

def astar (start,end):
    came_from = {}
    opened = set([start])
    closed = set()
    g = {start : 0}
    f = {start : hn[start]}
    while opened:
        current = None
        currentFx = None
        for node in opened:
            if current is None and f[node] < currentFx:
                current = node
                currentFx = f[node]
            if current == end:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                return path
        opened.remove(current)
        closed.add(current)