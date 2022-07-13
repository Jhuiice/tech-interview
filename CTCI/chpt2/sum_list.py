# Remove duplicates from an unsorted linked list
# Bonus: How would you do it without a buffer
from collections import deque


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


# def sum_list(head1, head2):
#     # this is the "cheat" method
#     head1 = reverse(head1)
#     head2 = reverse(head2)

#     sum_str1 = ""
#     sum_str2 = ""
#     while head1:
#         sum_str1 += str(head1.value)
#         head1 = head1.next

#     while head2:
#         sum_str2 += str(head2.value)
#         head2 = head2.next

#     return int(sum_str1) + int(sum_str2)

def sum_list(l1, l2):
    def addList(l1, l2, carry):
        if l1 == None and l2 == None and carry == 0:
            return None
        result = Node()
        value = carry

        if l1 is not None:
            value += l1.value

        if l2 is not None:
            value += l2.value

        result.data = value % 10
        print(result.data)

        # recurse
        if l1 != None or l2 != None:
            more = addList((None if l1 == None else l1.next),
                           (None if l1 == None else l2.next),
                           (1 if value >= 10 else 0))

            result.next = more
        print(result.data)
        return result  # returing none because it is at the end of the linked list

    return addList(l1, l2, 0)

    # l1_l2_sum = l1.value + l2.value + remainder
    # * I was going somewhere but not in the right direction
    # # print(l1_l2_sum)
    # # print(l1.value)
    # if l1_l2_sum > 9:
    #     ones = 1
    #     remainder = l1_l2_sum % 10
    # else:
    #     ones = l1_l2_sum
    #     remainder = 0
    # # print(l1.value)
    # l1.value = ones
    # print(l1.value)
    # if l1:
    #     l1 = l1.next
    # if l2:
    #     l2 = l2.nex


def reverse(head):
    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


def main():
    head = Node(7)
    head.next = Node(1)
    head.next.next = Node(6)

    head2 = Node(5)
    head2.next = Node(9)
    head2.next.next = Node(2)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = sum_list(head, head2)
    # print("Nodes of reversed LinkedList are: ", end='')
    print(result.value)


main()
