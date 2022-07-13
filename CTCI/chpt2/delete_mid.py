# delete a node in the middle of a singly linked list. Any node but the first and the last node.
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


def delete_mid(n):
    if n == None or n.next == None:
        return False
    # given only the node of the list how do I recconnect the list. How do I go back in time where the predessor node
    # doesn't know where to go?

    next = n.next
    n.data = next.data
    n.next = next.next
    return True


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(2)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(9)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = delete_mid(head, 5)
    print("Nodes of reversed LinkedList are: ", end='')
    head.print_list()
    result.print_list()


main()
