def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # turn it into a set and then calculate if n+1 is only +1 above value?
    # need to sort the array should I implement my own or just use the sort method?
#         set_nums = set(nums)
#         longest_consec = 0
#         for key, value in enumerate(set_nums):
    nums = set(nums)
    nums = sorted(nums)
    if len(nums) == 1:
        return 1
    if len(nums) == 0:
        return 0
    print(nums)
    # count = 0
    # temp = 1
    # nums.sort() # rememebr it does it with mutable data no return value
    # how do I deal with duplicates
    # remove them or make errosrs involved with them?
    # to do o(n) you can use the sort method
    # how do i keep track of the numbers?
#         for i in range(1, len(nums)):
#             if nums[i-1] + 1 == nums[i]:
#                 temp += 1
#             else:
#                 temp = 1
#             count = max(count, temp)

#         return count

    l, r, con = 0, 1, 0
    while r < len(nums):
        if nums[r-1] + 1 == nums[r]:
            r += 1
        else:
            l = r
            r += 1

        con = max(con, r - l)
    return con


arr = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

print(longestConsecutive(arr))
