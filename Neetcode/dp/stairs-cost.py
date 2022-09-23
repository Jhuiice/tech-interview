def minCostClimbingStairs(cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    # need to return minimal costs
    # check if costs of i or i+1 is less
    # _len = len(cost)
    # # combination of costs and steps
    # step_cost = 0
    # step_cost = cost[0] if cost[0] < cost[1] else cost[1]
    # i = 1 if step_cost == cost[0] else 2

    # while i < _len:
    #     # not grabbing last index
    #     print("i", i)
    #     if i+1 >= _len:
    #         step_cost += cost[i]
    #         break
    #     if i + 2 >= _len:
    #         i += 1
    #     elif cost[i+1] <= cost[i+2]:
    #         i += 1
    #     else:
    #         i += 2
    # print(_len)
    # while i + 2 < _len:
    #     # not grabbing last index
    #     print(i)
    #     if i + 2 < _len:
    #         if cost[i+1] < cost[i+2]:
    #             i += 1
    #         else:
    #             i += 2
    #     elif i + 1 > _len:
    #         break
    #     else:
    #         i += 1
    #     # print(i)
    #     step_cost += cost[i]
    # print("step_cost", step_cost)

    # return step_cost
    cost.append(0)
    for i in range(len(cost) - 3, -1, -1):
        cost[i] += min(cost[i+1], cost[i+2])

    return min(cost[0], cost[1])


arr = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]  # should compute to 6
arr1 = [10, 15, 20]


print(minCostClimbingStairs(arr))
# print(minCostClimbingStairs(arr1))
