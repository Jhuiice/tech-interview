from collections import deque


def maxAreaOfIsland(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # BFS implementation of islands
    # this can be a set or mark the graph that has been worked on
    # DFS is easier bc you can send in the row?
    visited = set()
    max_lands = 0

    def bfs(grid, r, c, visited):
        #             if !(0 >= r < len(grid) or 0 >= c < len(grid[0])):
        #                 return 0
        #             if grid[r][c] in visited or grid[r][c] == 0:
        #                 return 0

        #             visited.add(r,c)
        q = deque([(r, c)])
        count = 0
        while q:
            r, c = q.popleft()

            count += 1
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for a, b in directions:
                if not (0 <= (r + a) < len(grid) or 0 <= (c + b) < len(grid[0])) or grid[r+a][c+b] in visited or grid[r+a][c+b] == 0:
                    q.append((a, b))
                    visited.add((r, c))

        return count

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = bfs(grid, r, c, visited)
            if size > max_lands:
                max_lands = size
    return max_lands


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
    0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

print(maxAreaOfIsland(grid))
