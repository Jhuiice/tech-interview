# CTCI Magic Index 8.3

# can we cache the non distint numbers in a hash map?
# We can brute force this method and the time would be O(n)

def brute_force(nums):
    for i in range(len(nums)):
        if i == nums[i]:
            return True

    return False


# print(brute_force([1, 2, 3, 4, 5, 6, 7]))
# since its sorted we can use a binary search to find an index?
# if the numbers are non distinct once you get to an integer that is bigger than its index you can quit right there
# ? What if all the integers are smaller than its index? still take O(log(n))

# NOTE the below is not dynamic programming
# ? How do i implement dynamic programming?
def binary_search_non_distinct(nums):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + ((r - 1) // 2)
        print(l, m, r)

        if nums[m] > m:
            r = m - 1
        elif nums[m] < m:
            l = m + 1
        else:
            return True
        # ? Could I optimize this for non distinct nums?
        # * Dynamic Programming
    return False


# print(binary_search_non_distinct([-1, 0, 2, 3, 9, 12]))
# print(binary_search_non_distinct([-1, 0, 3, 4, 5, 5]))
print(binary_search_non_distinct([-1, 0, 3, 4, 5, 6, 7, 7]))
# print(binary_search_non_distinct([-1, 0, 2, 3, 4, 5]))

# ! The non-distinct problem set is a recursion to both sides of the array. min(minIndex - 1, leftIndex)
# ! than it would return the left value or recurse through the right based on its finding.
# ! compare the value upfront to the index i == A[i]
