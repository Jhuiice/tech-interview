from collections import deque


def shortest_path(edges, src, dst):
    graph = build_graph(edges)
    queue = deque([(src, 0)])
    visited = set([src])

    while len(queue) > 0:
        current, length = queue.pop()

        if current == dst:
            return length

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.appendleft((neighbor, length + 1))

    return -1


def build_graph(edges):
    graph = {}
    for a, b in edges:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph


edges = [
    ['w', 'x'],
    ['w', 'v'],
    ['x', 'y'],
    ['y', 'z'],
    ['v', 'z']
]

print(shortest_path(edges, 'w', 'z'))
