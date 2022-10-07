def gridTraveler(m, n, memo={}):
    key = str(m) + ',' + str(n)
    if key in memo:
        return memo[key]

    # base case one does not succeed
    if m == 0 or n == 0:
        return 0
    # base case two this is a winner
    if m == 1 and n == 1:
        return 1

    memo[key] = gridTraveler(m-1, n, memo) + gridTraveler(m, n-1, memo)
    return memo[key]


print(gridTraveler(0, 0))
print(gridTraveler(1, 1))
print(gridTraveler(2, 3))
print(gridTraveler(3, 3))
print(gridTraveler(18, 18))
