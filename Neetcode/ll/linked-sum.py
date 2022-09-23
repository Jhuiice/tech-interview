class Node():
    def __init__(self, val=None):
        self.val = val
        self.next = None


node = Node(0)
node.next = Node(1)
node.next.next = Node(2)
node.next.next.next = Node(3)


def linkedSum(l1, l2):
    # l1 = reverse(l1)
    # l2 = reverse(l2)

    # concatinate the values of the linkedlist
    # l1_string = ""
    # l2_string = ""

    # while l1:
    #     l1_string += str(l1.val)
    #     l2_string += str(l1.val)
    #     l1 = l1.next
    #     l2 = l2.next

    # for _ in range(0,2):

    cur = Node()
    dummy = cur

    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # sum
        val = val1 + val2 + carry
        carry = val // 10
        val = val % 10
        cur.next = Node(val)

        # new pointers
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        cur = cur.next
    return dummy.next

# def reverse(head):
#     next = head
#     prev = None
#     while head:
#         next = head.next
#         head.next = prev
#         prev = head
#         head = next
#     return prev
# reversed_node = reverse(node)
# while reversed_node:
#     print(reversed_node.val)
#     reversed_node = reversed_node.next


l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)

l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

_sum = (linkedSum(l1, l2))

while _sum:
    print(_sum.val)
    _sum = _sum.next
