def islands(graph):

    visited = set()  # ! to reduce space complexity you can manipulate the graph to another value instead of 1
    #! and have that as your marker instead of set.
    num_islands = 0

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if explore(graph, i, j, visited):
                num_islands += 1

    return num_islands

# this is not optimized lmao


def explore(graph, row, col, visited):
    rowInbound = 0 <= row < len(graph)
    colInbound = 0 <= col < len(graph[0])

    if not rowInbound or not colInbound:
        return False

    if (row, col) in visited:
        return False

    if graph[row][col] == 0:
        return False

    visited.add((row, col))

    # * visited will tell you where to go
    # ? is this optimzed?
    explore(graph, row + 1, col, visited)
    explore(graph, row - 1, col, visited)
    explore(graph, row, col + 1, visited)
    explore(graph, row, col - 1, visited)

    return True


graph = [
    [0, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0]
]

print(islands(graph))
print(islands([[]]))
