# return the kth to last element of the linked list
# this will use a runner.
# we can start by using a runner and a counter to see how large the list is
# then we can use the coutner to subtract K elements from it. IE i = c - k
# i will be the iterations it goes through to return the kth to last element


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


# def return_k(ll, k):
#     count = 0
#     counter_ll = ll
#     while counter_ll != None:
#         count += 1
#         counter_ll = counter_ll.next

#     nth_element = count - k
#     # print(nth_element)

#     kth_ll = ll
#     for i in range(nth_element):
#         kth_ll = kth_ll.next

#     return kth_ll.value
#! this is a better answer. This contains less space from above and works in the O(n) fashion
def return_k(head, k):
    p1 = head
    p2 = head

    for i in range(k):
        p1 = p1.next

    while p1 != None:
        p1 = p1.next
        p2 = p2.next

    return p2.value


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(2)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(9)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = return_k(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    print(result)


main()
