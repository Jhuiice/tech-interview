def min_islands(graph):
    visited = set()
    min_islands = float('inf')

    def explore(graph, r, c, visited):
        rowInbound = 0 <= r < len(graph)
        colInbound = 0 <= c < len(graph[0])
        if not rowInbound or not colInbound:
            return 0
        if (r, c) in visited:
            return 0
        if graph[r][c] == 0:
            return 0

        visited.add((r, c))
        size = 1

        size += explore(graph, r-1, c, visited)
        size += explore(graph, r+1, c, visited)
        size += explore(graph, r, c-1, visited)
        size += explore(graph, r, c+1, visited)

        return size

    for r in range(len(graph)):
        for c in range(len(graph[0])):
            size = explore(graph, r, c, visited)
            if size != 0 and size < min_islands:
                min_islands = size
    return min_islands


graph = [
    [0, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0]
]

print(min_islands(graph))
