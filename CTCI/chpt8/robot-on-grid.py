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

# memo will keep track of the movements of the robot
# what if they get stuck? Then They would have to backtrack
# ! When returning False it backtracks to the latest call
# keep track of fail points and points visited


def robot_on_grid(grid, memo, x, y):
    if len(grid) == 1 and len(grid[0]) == 1:
        return True
    if len(grid) == y and len(grid[0] == x):
        return True
    if grid[y][x+1] != None:
        memo[y][x+1] = 0
        return robot_on_grid(grid, memo, x+1, y)
    elif grid[y+1][x] != None:
        memo[y+1][x] = 0
        return robot_on_grid(grid, memo, x, y+1)
    else:
        memo[y][x+1] = None
        memo[y+1][x] = None
        return robot_on_grid(grid, memo, x-1, y-1)


def memoize(grid):
    r = len(grid[0])
    c = len(grid)
    memo = [[0] * r] * c
    print(memo)
    return robot_on_grid(grid, memo, 0, 0)


memoize(grid)
