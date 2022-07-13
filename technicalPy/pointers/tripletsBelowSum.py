# triplets below sum (medium)

# first attempt (failed)

def triplet_with_smaller_sum(arr, target):
    count = 0
    arr.sort()
    # TODO: Write your code here
    for i in range(len(arr)):
        right = len(arr) - 1
        left = i + 1
        if i > 0 and arr[i] == arr[i-1]:
            continue

        while left < right:  # this is causing an infinite loop
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum > target:
                right -= 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
            elif current_sum < target:
                count += 1
                left += 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1

    return count

    # second attempt after looking at solution
    # we want to compare the results of left and right to be less than arr[i] - target = target_sum


def triplet_with_smaller_sum(arr, target):
    count = 0
    arr.sort()
    # TODO: Write your code here
    for i in range(len(arr)):
        right = len(arr) - 1
        left = i + 1
        target_sum = target - arr[i]

        while left < right:

            if arr[left] + arr[right] < target_sum:
                count += right - left
                left += 1

            else:
                right -= 1

    return count
