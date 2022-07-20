# pair with target sum (easy)

# time complexity is O(N)
# space complexity is 0(1)

# first attempt

def pair_with_targetsum(arr, target_sum):
    # TODO: Write your code here
    pointer_one = 0
    pointer_two = len(arr) - 1
    sum_of_pointers = 0
    while pointer_two - pointer_one != 0:
        sum_of_pointers = arr[pointer_one] + arr[pointer_two]
        if sum_of_pointers == target_sum:
            return [pointer_one, pointer_two]
        if sum_of_pointers > target_sum:
            pointer_two -= 1
        if sum_of_pointers < target_sum:
            pointer_one += 1

    return [-1, -1]


# grokking answer with pointers

def pair_with_targetsum(arr, target_sum):
    left, right = 0, len(arr) - 1
    while(left < right):
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [left, right]

        if target_sum > current_sum:
            left += 1  # we need a pair with a bigger sum
        else:
            right -= 1  # we need a pair with a smaller sum
    return [-1, -1]


def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))


main()


# grokking answer with hashtables
# time complexity is O(N)
# space complexity is O(N) this is a wee bit larget than the pointer method
# this method would be good to know if you want to describe another method with a different time complexity
def pair_with_targetsum(arr, target_sum):
    nums = {}  # to store numbers and their indices
    for i, num in enumerate(arr):  # would need to learn enumerate
        if target_sum - num in nums:
            return [nums[target_sum - num], i]
        else:
            nums[arr[i]] = i
    return [-1, -1]


def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))


main()
