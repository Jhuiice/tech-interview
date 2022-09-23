def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # memo the last i-1 steps
    # the index can start on i = 1 or i = 0
    # can take the max of two recursive functions one starting at i = 1 and one at i = 0
    # but its not always going to be every other one.
    # what do i check what subproblems do i compare?
    # you can jump one or two but never want to jump three because of a missing link
    # it will be a combinations of
    # i: 0,2[4,5]
    # i: 1,[3[5[7,8],6[8,9]],4[6,7],5[7[9,10],8[10,11]]]
    # brute force would be n^2 because every branch can branch out twice.

    # [[0],[1],[0,2],[0,3],[1,3],[1,4]]

    # how do I calculate with 2 different starting nodes?
    if len(nums) == 0:
        return 0

    # def start_r(nums):
    #     return r_r(nums, 0)

    # def r_r(nums, startIndex):
    #     if startIndex >= len(nums):
    #         return 0

    #     root1 = nums[startIndex] + \
    #         max(r_r(nums, startIndex+2), r_r(nums, startIndex+3))
    #     startIndex += 1
    #     if startIndex >= len(nums):
    #         return root1
    #     root2 = nums[startIndex] + \
    #         max(r_r(nums, startIndex+2), r_r(nums, startIndex+3))
    #     print(root1, root2)
    #     return max(root1, root2)

    # return start_r(nums)
    contains = [nums[0]]
    vacant = [0]

    for i in range(1, len(nums)):
        contains.append(vacant[i-1] + nums[i])
        vacant.append(max(vacant[i-1], contains[i-1]))

    return max(contains[-1], vacant[-1])


nums1 = [2, 7, 9, 3, 1, 4, 5, 10]
nums = [183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238,
        168, 128, 177, 235, 50, 81, 185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]


print(rob(nums))
print(rob(nums1))
