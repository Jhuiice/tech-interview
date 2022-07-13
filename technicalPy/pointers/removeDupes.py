# remove duplicates (easy)

# first attempt
def remove_duplicates(arr):
    # TODO: Write your code here
    # i am using pointers. How do I do this?
    # point to one spot and then move the next
    # i can use a hash map and make it but that is using more space
    # ill have to keep track the next index with a pointer. What is the most efficient way for that?
    # edge cases
    if not arr:
        return 0
    if len(arr) == 1:
        return 1
    # left is the left index pointer
    for left in range(len(arr)):
        current = arr[left]
        if left + 1 > len(arr) - 1:
            break
        _next = arr[left + 1]
        if current == _next:
            for j in range(left + 1, len(arr) - 1):
                arr[j] = arr[j + 1]
            # arr.pop()
            print(arr)

        return len(arr)

    return -1


def remove_dupes(arr):
    pass


# actual grokking

def remove_duplicates(arr):
    # index of the next non-duplicate element
    next_non_duplicate = 1

    i = 0
    while(i < len(arr)):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1

    return next_non_duplicate


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()


# 2nd attempt
def make_squares(arr):
    # create the squares array with list comprehension to mirror the size of the input arr

    squares = [0 for x in arr]
    n = len(squares)
    left, right = 0, n - 1
    maximum_index = n - 1
    # TODO: Write your code here
    while left <= right:
        left_square = arr[left] ** 2
        right_square = arr[right] ** 2

        if left_square > right_square:
            squares[maximum_index] = left_square
            left += 1

        if right_square >= left_square:
            squares[maximum_index] = right_square
            right -= 1

        maximum_index -= 1

    return squares
