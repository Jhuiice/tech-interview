class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None


# cant do the below because of edge cases with lengths of linked lists of 1 and 2
def remove_nth_node(head, n):
    dummy, left, right = head, head, head

    while n >= 0:
        right = right.next
        n -= 1

    while right:
        right = right.next
        left = left.next

    left.next = left.next.next

    return dummy


node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(4)
node.next.next.next.next = Node(5)

# print(remove_nth_node(node, 2))
head = remove_nth_node(node, 2)
while head:
    print(head.data)
    head = head.next
