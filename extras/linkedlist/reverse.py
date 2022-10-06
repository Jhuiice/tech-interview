class Node():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse(head):
    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next

    return prev


one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
one_temp = one

one.next = two
two.next = three
three.next = four
while one_temp:
    print(one_temp.val)
    one_temp = one_temp.next
rev = reverse(one)
while rev:
    print(rev.val)
    rev = rev.next
