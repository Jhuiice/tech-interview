def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) == 0 or len(prices) == 1:
        return 0
    i, j = 0, 1
    # how to buy? On what circumstances?
    # check the right - left attributes
    # save it in a sum called profit
    # do i need any data strucutes
    # when do i move pointers?
    # if right is less than left or right is greater than right

    profit = 0
    while j < len(prices):
        left = prices[i]
        right = prices[j]

        if left > right:
            i += 1

        if right > left:
            if right - left > profit:
                profit = right - left

        # print(profit, i, j)
        j += 1
    if profit <= 0:
        return 0
    return profit


print(maxProfit([1, 2, 4]))
