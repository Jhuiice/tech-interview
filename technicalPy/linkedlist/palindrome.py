# grokking
#Palindrome LinkedList (medium)#

# Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

# Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. The algorithm should have O(N)O(N)O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.


# first attempt
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head):
    # TODO: Write your code here
    # can you come from the right side of the linked List? Or is the head the only starting point?
    # have a pointer to start form the middle of the linked list
    # had one pointer going forward and one pointer being recet to K - 1 nodes for every set
    # we would need the length of the list first to get knodes ahead of
    left_pointer = head
    # right_pointer = head
    fast, slow = head, head
    linked_length = return_length_list(head)
    # print(linked_length)
    # counters are using space.
    k = 0
    right_counter = linked_length
    # now we must get to k Nodes away (end => middle)
    while k < linked_length:
        right_pointer = head
        count = 0
        while count < right_counter:
            right_pointer = right_pointer.next
            count += 1
        print(left_pointer.value, right_pointer.value)

        if right_pointer.value != left_pointer.value:
            break

        left_pointer = left_pointer.next

        if right_counter == 1:
            return True
        k += 1
        right_counter -= 1

    return False


def return_length_list(head):
    pointer = head
    _length = 0
    while pointer is not None and pointer.next is not None:
        _length += 1
        pointer = pointer.next

    return _length


def get_nodes(head, _length):
    k = 0
    while k < _length:
        head = head.next


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()


# class Node:
#   def __init__(self, value, next=None):
#     self.value = value
#     self.next = next


def is_palindromic_linked_list(head):
    if head is None or head.next is None:
        return True

    # find middle of the LinkedList
    slow, fast = head, head
    while (fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next

    head_second_half = reverse(slow)  # reverse the second half
    # store the head of reversed part to revert back later
    copy_head_second_half = head_second_half

    # compare the first and the second half
    while (head is not None and head_second_half is not None):
        if head.value != head_second_half.value:
            break  # not a palindrome

        head = head.next
        head_second_half = head_second_half.next

    reverse(copy_head_second_half)  # revert the reverse of the second half

    if head is None or head_second_half is None:  # if both halves match
        return True

    return False

# reversed it from the middle


def reverse(head):
    prev = None
    while (head is not None):
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()
