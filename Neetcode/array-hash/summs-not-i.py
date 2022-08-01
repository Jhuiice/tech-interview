def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # sliding window? no because you would need division unless you started from the end?
    # need all elements from the left and the right except for self
    sums = [1] * (len(nums))
    # for i in range(len(nums)):
    #     summ = 1
    #     l = i - 1
    #     r = i + 1
    #     while l > 0 or r <= len(nums) - 1:

    #         if l >= 0:
    #             summ *= nums[l]
    #             l -= 1
    #         if r <= len(nums) - 1:
    #             summ *= nums[r]
    #             r += 1
    #         print(l, r)
    #     sums.append(summ)

    for i in range(0, len(nums)):
        summ = 1
        for j in range(0, i):
            summ *= nums[j]
        for k in range(i + 1, len(nums)):
            summ *= nums[k]

        sums[i] = summ

    return sums


print(productExceptSelf([2, 3, 4, 5, 6]))
print(productExceptSelf([0, 0]))
