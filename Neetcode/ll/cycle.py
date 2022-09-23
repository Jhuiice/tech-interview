class Node():
    def __init__(self, val=0):
        self.val = val
        self.next = None


cycle_node = Node(4)
cycle_node_1 = Node(1)
node = Node(0)
node.next = cycle_node_1
cycle_node_1.next = Node(2)
node.next.next.next = Node(3)
node.next.next.next.next = cycle_node
cycle_node.next = cycle_node_1


def findCycle(head):
    r1, r2 = head, head
    # r1 = r1.next
    # print(r1.val, head.val)
    # while T

    while r1 != None and r1.next != None:
        r1 = r1.next.next
        r2 = r2.next
        if r1.val == r2.val:
            return True
        return False


print(findCycle(node))
