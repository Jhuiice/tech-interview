# triples sum close to target

# first attempt
import math


def triplet_sum_close_to_target(arr, target_sum):
    # TODO: Write your code here
    # keep track of the sum
    arr.sort()
    triplets = []
    # very dependent variable. It would only work in a few test cases use math.inf
    closest_value = target_sum
    for i in range(len(arr)):
        right = len(arr) - 1
        left = i + 1

        # check the value of the sum of the array

        while left < right:
            current_sum = arr[right] + arr[left] + arr[i]
            difference = target_sum - current_sum
            if difference < 0:
                difference = -difference
            if difference < closest_value:
                closest_value = difference
                triplets = [arr[right], arr[left], arr[i]]

            if current_sum == target_sum:
                return current_sum
            elif current_sum > target_sum:
                right -= 1
            else:
                left += 1

    return sum(triplets)


# grokking attempt


def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    smallest_difference = math.inf
    for i in range(len(arr)-2):
        left = i + 1
        right = len(arr) - 1
        while (left < right):
            target_diff = target_sum - arr[i] - arr[left] - arr[right]
            if target_diff == 0:  # we've found a triplet with an exact sum
                return target_sum  # return sum of all the numbers

            # the second part of the following 'if' is to handle the smallest sum when we have more than one solution
            if abs(target_diff) < abs(smallest_difference) or (abs(target_diff) == abs(smallest_difference) and target_diff > smallest_difference):
                smallest_difference = target_diff  # save the closest and the biggest difference

            if target_diff > 0:
                left += 1  # we need a triplet with a bigger sum
            else:
                right -= 1  # we need a triplet with a smaller sum

    return target_sum - smallest_difference


def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()
