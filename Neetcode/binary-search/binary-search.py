def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # l = len(nums)
    # mid = l // 2
    l = len(nums)
    mid = l // 2
    temp = nums
    while mid != 0 and l > 1:
        l = len(nums)
        mid = l // 2 - 1
        print(l, mid)
        print(nums[mid], "mid")
        if target == temp[mid]:
            return target
        elif target > temp[mid]:
            temp = temp[:mid]
        else:
            temp = temp[mid+1:]

    return -1


# print(search([-1, 0, 3, 5, 9, 12], 9))


def search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + ((r - l) // 2)
        # print("left, right, mid", l, r, m)  # (l + r) // 2 can lead to overflow
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    return -1


print(search([-1, 0, 3, 5, 9, 12], 9))
print(search([5], 5))
