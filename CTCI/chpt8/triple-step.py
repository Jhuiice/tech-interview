# CTCI Triple Step 8.1

# num of steps = num of permutations
# 1 = 1 (1)
# 2 = 2 (1,1), (2)
# 3 = 4 (1,1,1), (1,2), (2,1), (3)
# 4 = 7 (1,1,1,1), (1,1,2), (1,2,1), (2,1,1), (2,2), (3,1), (1,3)
# 5 = 13 (1,1,1,1,1), (1,1,1,2), (1,1,2,1), (1,2,1,1) (2,1,1,1), (2,2,1), (2,1,2), (1,2,2), (3,1,1), (1,3,1) (1,1,3), (3,2), (2,3)
# 6 = (1,1,1,1,1,1), (1,1,1,1,2) * 5, (1,1,1,3) * 4, (3,2,1),(3,1,2),(2,3,1),(2,1,3),(1,2,3),(1,3,2), (2,2,2), (3,3)

from itertools import count


def triple_step_bottom_up(n):
    if n == 1 or n == 0:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    # ? how many combinations are there between steps. is there a ceiling for combinations?
    bottom_up = [None] * (n + 1)
    bottom_up[1] = 1
    bottom_up[2] = 2
    bottom_up[3] = 4

    for i in range(4, n+1):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2] + bottom_up[i - 3]
    return bottom_up[i]


print(triple_step_bottom_up(5))
print(triple_step_bottom_up(6))
print(triple_step_bottom_up(7))


def triple_step_top_down(n, memo):
    if memo[n] < 0:
        return 0
    elif n == 0:
        return 1
    elif memo[n] > -1:
        return memo[n]
    else:
        memo[n] = triple_step_top_down(
            n-1, memo) + triple_step_top_down(n-2, memo) + triple_step_top_down(n-3, memo)
        return memo[n]


def memoize(n):
    memo = [-1] * (n + 1)
    return triple_step_top_down(n, memo)


print(memoize(5))
print(memoize(6))
print(memoize(7))


def count_ways(n):
    if (n < 0):
        return 0
    elif n == 0:
        return 1
    else:
        return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)


# print(count_ways(6))
# print(count_ways(8))
