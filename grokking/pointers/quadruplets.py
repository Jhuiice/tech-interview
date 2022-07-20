#Quadruple Sum to Target (medium)#

# Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.

# first attempt (failed)

def search_quadruplets(arr, target):
    quadruplets = []
    # TODO: Write your code here
    # do we need a 4th pointer? or are we going to use a while loop to get numbers inbetween the two pointers
    arr.sort()
    for i in range(len(arr) - 3):
        if i > 0 and arr[i] == arr[i-1]:
            continue

        for j in range(len(arr) - 2):
            if j > i + 1 and arr[j] == arr[j-1]:
                continue
            # call another function
            sum_quads(i, j, target, arr, quadruplets)
    return quadruplets


def sum_quads(first, second, target, arr, quadruplets):
    left = second + 1
    right = len(arr) - 1
    while left < right:
        quad_sum = arr[first] + arr[second] + arr[left] + arr[right]

        if quad_sum == target:
            quadruplets.append(
                [arr[first], arr[second], arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1

        elif quad_sum > target:
            right -= 1
        else:
            left += 1

# SOLUTION FROM GROKKING


def search_quadruplets(arr, target):
    arr.sort()
    quadruplets = []
    for i in range(0, len(arr)-3):
        # skip same element to avoid duplicate quadruplets
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        for j in range(i + 1, len(arr)-2):
            # skip same element to avoid duplicate quadruplets
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue
            search_pairs(arr, target, i, j, quadruplets)
    return quadruplets


def search_pairs(arr, target, first, second, quadruplets):
    left = second + 1
    right = len(arr) - 1
    while (left < right):
        quad_sum = arr[first] + arr[second] + arr[left] + arr[right]
        if quad_sum == target:  # found the quadruplet
            quadruplets.append(
                [arr[first], arr[second], arr[left], arr[right]])
            left += 1
            right -= 1
            while (left < right and arr[left] == arr[left - 1]):
                left += 1  # skip same element to avoid duplicate quadruplets
            while (left < right and arr[right] == arr[right + 1]):
                right -= 1  # skip same element to avoid duplicate quadruplets
        elif quad_sum < target:
            left += 1  # we need a pair with a bigger sum
        else:
            right -= 1  # we need a pair with a smaller sum


def main():
    print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
    print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))


main()
