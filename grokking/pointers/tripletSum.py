# triplet sum to zero (medium)

# first attempt after viewing solution

def search_triplets(arr):
    triplets = []
    # TODO: Write your code here
    # have two pointers and a sum
    # the target sum is the negative value of the current value of the index of the array
    # how would I iterate through this? it would be a while loop within a for loop
    # the right pointer is far right
    # unsorted so we would need to sort it
    arr.sort()
    for i in range(len(arr)):
        target_sum = -arr[i]  # this value but negative
        left = i + 1
        # have declaration of right pointer in for loop becuase it always needs to be reset to original value
        right = len(arr) - 1
        # check if the next value is a duplicate
        if i > 0 and arr[i-1] == arr[i]:
            continue

        while left < right:
            current_sum = arr[left] + arr[right]
            if target_sum == current_sum:
                triplets.append([-target_sum, arr[left], arr[right]])
                left += 1
                right -= 1
                # skip duplicates for left and right using two while loops
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

            elif target_sum > current_sum:
                left += 1
            else:
                right -= 1

        #
    print(triplets)
    return triplets


# grokking actual answer

def search_triplets(arr):
    arr.sort()
    triplets = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:  # skip same element to avoid duplicate triplets
            continue
        search_pair(arr, -arr[i], i+1, triplets)

    return triplets


def search_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1
    while(left < right):
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:  # found the triplet
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1  # skip same element to avoid duplicate triplets
            while left < right and arr[right] == arr[right + 1]:
                right -= 1  # skip same element to avoid duplicate triplets
        elif target_sum > current_sum:
            left += 1  # we need a pair with a bigger sum
        else:
            right -= 1  # we need a pair with a smaller sum


def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))


main()
