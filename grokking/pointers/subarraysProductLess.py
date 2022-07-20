# Subarrays with Product Less than a Target (medium)

# Problem Statement#

# Given an array with positive numbers and a positive target number, find all of its contiguous subarrays whose product is less than the target number.

# first attempt

# brute force I should have used pointers and a sliding glass window
from collections import deque


def find_subarrays(arr, target):
    result = []
    # arr.sort()
    # TODO: Write your code here
    for i in range(len(arr)):
        right = i + 1
        left = i

        if i > 0 and arr[i] == arr[i-1]:
            continue

        if arr[i] < target:
            result.append([arr[i]])

        if i > 0 and arr[i] * arr[i-1] < target:
            result.append([arr[i-1], arr[i]])

    return result

    # grokking solution used a deque to pop accordingly


def find_subarrays(arr, target):
    result = []
    product = 1
    left = 0
    for right in range(len(arr)):
        product *= arr[right]
        while (product >= target and left < len(arr)):
            product /= arr[left]
            left += 1
        # since the product of all numbers from left to right is less than the target therefore,
        # all subarrays from left to right will have a product less than the target too; to avoid
        # duplicates, we will start with a subarray containing only arr[right] and then extend it
        temp_list = deque()
        for i in range(right, left-1, -1):
            temp_list.appendleft(arr[i])
            result.append(list(temp_list))
    return result


def main():
    print(find_subarrays([2, 5, 3, 10], 30))
    print(find_subarrays([8, 2, 6, 5], 50))


main()
