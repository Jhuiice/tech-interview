# this is a memory pull of merge sort and CTCI Concepts
# DATE: 6/29/2022

# data structures i need to remember
# * Strings/arrays, hash maps, heaps, tree/trie/graphs, linked lists, stacks and queues

# algorithms i must rememebr
# * Binary search, quick sort, merge sort, Breadth first search, depth first search, insertion sort

# concepts I must remember
# * Recursion, memory(stack vs queues), bit manipulation, dynamic programming, big O time and space complexity

# This is the merge sort lets see how much I can create

# nuances
# # left starts at index 0
# # right starts at len(arr) - 1

# merge is the first function to be called then mergeSort is called for the left side array and the right side array
# mid is calclulated inside of mergeSort as mid = left + (right - left) // 2

def merge(arr, left, mid, right):
    n1 = mid - left + 1  # the size of the left and right of the array
    n2 = right - mid  # the size of the right array moment

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[left + i]

    for j in range(0, n2):
        R[j] = arr[j + mid + 1]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)


arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is")
for i in range(n):
    print("%d" % arr[i], end=" ")

mergeSort(arr, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arr[i], end=" ")
print()
