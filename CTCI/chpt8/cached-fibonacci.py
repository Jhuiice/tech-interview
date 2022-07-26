def fibonacci1(n):
    memo = [0] * (n+1)
    return fibonacci(n, memo)


def fibonacci(i, memo):
    if i == 0 or i == 1:
        return i
    # * The act of storing computed values for future is called memoization a form of cacheing
    if memo[i] == 0:
        memo[i] = fibonacci(i-1, memo) + fibonacci(i-2, memo)

    return memo[i]


# print(fibonacci1(5))
# print(fibonacci1(6))
# print(fibonacci1(7))
# print(fibonacci1(8))
# print(fibonacci1(9))
# print(fibonacci1(10))
# print(fibonacci1(11))
# print(fibonacci1(12))
# print(fibonacci1(13))
# print(fibonacci1(14))
# print(fibonacci1(15))
# print(fibonacci1(16))

def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n + 1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n + 1):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]
    return bottom_up[n]


print(fib_bottom_up(5))
print(fib_bottom_up(7))
print(fib_bottom_up(9))


def fib_top_down(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        return 1
    else:
        result = fib_top_down(n-1, memo) + fib_top_down(n-2, memo)
        memo[n] = result
    return result


def fib_memo(n):
    memo = [None] * (n + 1)
    return fib_top_down(n, memo)


print(fib_memo(5))
print(fib_memo(7))
print(fib_memo(9))
