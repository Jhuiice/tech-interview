# CTCI Robot On Grid CTCI 8.2

# def robot_on_grid(r, c, off_limits):
# robot starts at top left [0,0] on a grid.
# robot can move right and down
# certain cells are off limits to move to
# brute force it to use a while loop until it hits the bottom right or r and c are both errors
# memoization is already here with the off_limits peace?
# find a path. So i can use the bottom_up approach and keep it in an array or add to an array[n] of new position
# * This is a matrix problem
# * r = 3, x = 5
# [
#     [0, None, 0, 0, 0],
#     [0, 0, 0, 0, None],
#     [None, None, None, 0, 0]
# ]
# x, y = 0, 0
# while x != len(y) or y != len(c):
#     # * grid points will be
#     # if grid[0][x+1] != None:
#     # move right
#     pass

# robot place = grid[0][0]
# if grid[y][x+1] != None:
#   movement[n] = movement[n-1] + "right"
#   return robot_on_grid(x+1, y, movement, grid)
# elif grid[y+1][x] != None:
#   movement[n] = movement[n-1] + "down"
#   return robot_on_grid(x, y+1, movement, grid)
# else:
#   return movement


# would it be a grid to memoize or an array that i appened right and left onto?
# lets do a grid approach
grid = [
    [0, None, 0, 0, 0],
    [0, 0, 0, 0, None],
    [None, None, None, 0, 0]
]
grid2 = [
    [0, None, 0, 0, 0],
    [0, 0, 0, 0, None],
    [None, None, None, 0, None]
]

grid3 = [
    [0, None, 0, 0, 0],
    [0, None, 0, 0, None],
    [None, None, None, 0, 0]
]
grid4 = [
    [None, None, None, None, None],
    [None, None, None, None, None],
    [None, None, None, None, 0]
]
# memo will keep track of the movements of the robot
# what if they get stuck? Then They would have to backtrack
# ! When returning False it backtracks to the latest call
# keep track of fail points and points visited


# def robot_on_grid(grid, memo, x, y):
#     if len(grid) == 1 and len(grid[0]) == 1:
#         return True
#     if len(grid) == y and len(grid[0] == x):
#         return True
#     if grid[y][x+1] != None:
#         memo[y][x+1] = 0
#         return robot_on_grid(grid, memo, x+1, y)
#     elif grid[y+1][x] != None:
#         memo[y+1][x] = 0
#         return robot_on_grid(grid, memo, x, y+1)
#     else:
#         memo[y][x+1] = None
#         memo[y+1][x] = None
#         return robot_on_grid(grid, memo, x-1, y-1)


# def memoize(grid):
#     r = len(grid[0])
#     c = len(grid)
#     memo = [[0] * r] * c
#     print(memo)
#     return robot_on_grid(grid, memo, 0, 0)


# memoize(grid)
# bottom_up_approach is iterative it will use a while loop
def robot_on_grid(grid, r, c):
    visited = [(0, 0)]
    blocked = {}  # {(r,c): False}
    if grid[-1][-1] == None:
        return False

    while r != len(grid) - 1 and r != len(grid[-1]) - 1:
        if grid[r][c+1] != None and (r, c+1) not in blocked:
            c = c+1
            visited.append((r, c))

        elif grid[r+1][c] != None and (r+1, c) not in blocked:
            r = r+1
            visited.append((r, c))

        elif grid[r+1][c] == None and grid[r][c+1] == None:
            blocked[(r, c)] = True
            visited.pop()
            print(visited)
            r = visited[-1][0]
            c = visited[-1][1]
        else:
            return False
        # if grid[r][c] == grid[-1][-1] and grid[-1]
        print(r, c)

    return True


print(robot_on_grid(grid, 0, 0))
print(robot_on_grid(grid2, 0, 0))
print(robot_on_grid(grid3, 0, 0))
print(robot_on_grid(grid4, 0, 0))
