def largest_compt(graph):
    visited = set()
    largest = -1
    count = 0

    for node in graph:
        count = explore(graph, node, visited)
        largest = max(largest, count)

    return largest


# def explore(graph, current, visited, count): can do this way or
def explore(graph, current, visited):
    if current in visited:
        # return count
        return 0
    visited.add(current)

    size = 1  # * When this gets called for the first time it will be at the head of the stack
    for neighbor in graph[current]:
        # * size is incrememted with every connected node in the component
        size += explore(graph, neighbor, visited)

    return size


# * undirected graph
graph = {
    0: [8, 1, 5],
    1: [0],
    2: [3, 4],
    3: [2, 4],
    4: [2, 3],
    5: [8, 0],
    8: [5, 0]
}

print(largest_compt(graph))
