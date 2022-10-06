def fib_tab(n):
    memo = [0] * (n + 1)
    memo[1] = 1
    memo[2] = 1

    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]


def fib_memo(n, memo={}):
    if (n in memo):
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]


# print(fib_tab(5))
# print(fib_tab(6))
# print(fib_tab(7))
# print(fib_tab(8))
# print(fib_tab(50))
print(fib_memo(5))
print(fib_memo(6))
print(fib_memo(7))
print(fib_memo(8))
print(fib_memo(50))
