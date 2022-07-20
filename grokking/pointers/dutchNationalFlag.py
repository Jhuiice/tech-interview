# Dutch National Flag Problem (medium)
#Problem Statement#

# Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

# The flag of the Netherlands consists of three colors: red, white and blue; and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.

# first attempt after looking at solution
# if the left value is 2 you swithc the left and right value
# if the right have value is a 0 you switch left and right indices

# use a while loop to sort with pointers
# Time complexity is O(N)
# Space Complexity is O(1)

def dutch_flag_sort(arr):
    # TODO: Write your code here
    left, right = 0, len(arr) - 1
    i = 0
    while i <= right:
        if arr[i] == 0:
            arr[i], arr[left] = arr[left], arr[i]
            i += 1
            left += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i], arr[right] = arr[right], arr[i]
            right -= 1

    return arr
