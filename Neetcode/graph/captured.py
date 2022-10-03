from collections import deque

# code works! not very fast though


def solve(board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    visited = set()

    def explore(grid, r, c, visited):
        q = deque([(r, c)])
        outOfBounds = False
        visit = []
        while q:
            r, c = q.pop()
            if (r, c) not in visited:
                visited.add((r, c))
                visit.append((r, c))
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for direct in directions:
                    row, col = direct[0], direct[1]
                    rowInbound = 0 <= r+row < len(grid)
                    colInbound = 0 <= c+col < len(grid[0])
                    if (rowInbound and colInbound):
                        if grid[r+row][c+col] == 'O':
                            q.appendleft((r+row, c+col))
                    else:
                        outOfBounds = True

        if not outOfBounds:
            for node in visit:
                row, col = node[0], node[1]
                grid[row][col] = 'X'

    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 'O':
                explore(board, r, c, visited)

    return board


board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
         ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
# board = [
#     ["O", "X", "X", "O", "X"],
#     ["X", "O", "O", "X", "O"],
#     ["X", "O", "X", "O", "X"],
#     ["O", "X", "O", "O", "O"],
#     ["X", "X", "O", "X", "O"]
# ]

expected = [
    ["O", "X", "X", "O", "X"],
    ["X", "X", "X", "X", "O"],
    ["X", "X", "X", "O", "X"],
    ["O", "X", "O", "O", "O"],
    ["X", "X", "O", "X", "O"]
]

actual = [
    ['O', 'X', 'X', 'O', 'X'],
    ['X', 'X', 'X', 'X', 'O'],
    ['X', 'X', 'X', 'O', 'X'],
    ['O', 'X', 'X', 'X', 'O'],
    ['X', 'X', 'O', 'X', 'O']
]

actual = [
    ["O", "X", "X", "O", "X"],
    ["X", "X", "X", "X", "O"],
    ["X", "X", "X", "O", "X"],
    ["O", "X", "O", "X", "O"],
    ["X", "X", "O", "X", "O"]
]


print(solve(board))
