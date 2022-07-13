# Excersises for chapter 2.1

def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key

    return arr


print(insertion([5, 2, 1, 6, 4, 3]))

# 2
# to descend an insertion sort you change the arr[j] < key
# to ascend an insertion sort you change the arr[j] > key


def reverseInsertion(arr):
    for i in range(0, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] < key:
            # print(j)
            arr[j + 1] = arr[j]
            # print(j, "j")
            j -= 1

        arr[j + 1] = key

    return arr


print(reverseInsertion([5, 2, 1, 6, 4, 3]))
