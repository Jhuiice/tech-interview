# Remove duplicates from an unsorted linked list
# Bonus: How would you do it without a buffer
from collections import deque


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def remove_dupes(ll):
    # how am I going to keep track of data? Hashmap/Dictionary What is the time complexity of this method?
    # I can create another list of the objects that are not in the list but what is the space complexity of that?
    # non_duplicates = deque([])
    # for item in ll:
    #     if item not in non_duplicates:
    #         non_duplicates.append(item)

    # return non_duplicates

    # how would I do this in place?
    dup_list = []
    prev = Node(None)
    while ll != None:

        if ll.value in dup_list:
            prev.next = ll.next
        else:
            dup_list.append(ll.value)
            prev = ll
            print(prev.value)
        # print(ll.value)
        # print(prev.value)
        ll = ll.next
    return prev


def remove_dupes_unbuffer(head):
    current = head
    while current != None:
        runner = current
        while runner.next != None:
            if runner.next.value == current.data:
                runner.next = runner.next.next
            else:
                current = current.next
# this code takes O(1) space but O(n^2) time

# ll = deque([6, 1, 4, 7, 2, 1, 6])
# print(remove_dupes(ll))


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(2)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(9)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = remove_dupes(head)
    print("Nodes of reversed LinkedList are: ", end='')
    print(result.print_list())


main()
