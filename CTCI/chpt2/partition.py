# Partition the linked list based off of x# delete a node in the middle of a singly linked list. Any node but the first and the last node.
# get the exact middle node if possible

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


# def partition(head, x):
#     pass1 = head
#     pass2 = head
#     current = Node(None)
    # use two run throughs of the list making it O(N) this is no the most optimal way
    # you can squeeze list items inbetween eachother
    # while pass1 != None:
    #     if pass1.value < x:
    #         current.next = pass1
    #         current = current.next
    #         print("Value", current.value)
    #     # print(pass1.value)
    #     pass1 = pass1.next
    # while pass2 != None:
    #     if pass2.value >= x:
    #         current.next = pass2
    #         current = current.next
    #         print("Value in loop 2", current.value)
    #     pass2 = pass2.next

    # node value
    # node.next is greater than x
    # node is less than x
    # how can I squeeze this inbetween themselves?
    # node.next.next = value greater than x?
    # node.next = vaue less than x?

def partition(head, x):
    # objects are passed by reference in this declaration Why do we have an extra node?
    before = before_head = Node(0)
    after = after_head = Node(0)
    # before.print_list()
    # before_head.print_list()

    while head:
        # If the original list node is lesser than the given x,
        # assign it to the before list.
        if head.value < x:
            before.next = head
            before = before.next
        else:
            # If the original list node is greater or equal to the given x,
            # assign it to the after list.
            after.next = head
            after = after.next

        # move ahead in the original list
        head = head.next

    # Last node of "after" list would also be ending node of the reformed list
    after.next = None
    # print("After")
    after.print_list()
    after_head.print_list()
    # Once all the nodes are correctly assigned to the two lists,
    # combine them to form a single list which would be returned.
    before.next = after_head.next

    return before_head.next

    # we need to add a list of nodes to a linked list that is less than x
    # we need to add to a list of nodes, nodes that are less than x in a linked list


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(2)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(9)
    head.next.next.next.next.next = Node(19)
    head.next.next.next.next.next.next = Node(2)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = partition(head, 5)
    print("Nodes of reversed LinkedList are: ", end='')
    # head.print_list()
    result.print_list()


main()
