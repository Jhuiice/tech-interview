# check if the linked-list is a palindrome
# this would be simple is the list was doubly linked

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


def palindrome(head):
    # get to the middle of the list
    # middle = head
    # reverse the middles of the list
    # first
    # then run through both lists and compare the outputs
    second_half = find_middle(head)
    second_half_reversed = reverse(second_half)

    while second_half_reversed is not None:
        first_char = head.value
        second_char = second_half_reversed.value
        print(first_char, second_char)
        if first_char != second_char:

            return False
        head = head.next
        second_half_reversed = second_half_reversed.next

    return True


def find_middle(head):
    current = head
    second_half = head
    count = 0
    mid = 0

    while current:
        current = current.next
        count += 1
    if count % 2 != 0:
        mid = count // 2 + 1
    else:
        mid = count // 2

    print("Count, Mid", count, mid)
    i = 0
    while i < mid:
        second_half = second_half.next
        i += 1

    return second_half


def reverse(head):
    current, next, prev = None, None, head.next

    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current.next = next

    return current


def main():
    head = Node("r")
    head.next = Node("a")
    head.next.next = Node("c")
    head.next.next.next = Node("e")
    head.next.next.next.next = Node("c")
    head.next.next.next.next.next = Node("a")
    head.next.next.next.next.next.next = Node("r")

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = palindrome(head)
    print("Nodes of reversed LinkedList are: ", end='')
    print(result)


main()
