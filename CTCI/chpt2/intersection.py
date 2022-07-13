# see if the node are instersecting at any point. This means the nodes are the exact same not the value data

# compare nodes if node1 == node2

# you can implement this over two for loops but that would make the time complexity O(N^2)
# can implement this recurively and compare?

# get the lengths of the linked lists and subtract the larger from the smaller
# start the longer list off with the difference of the two lists

# this will be a memory pull of my knowledge of linked lists
# Date July 6th, 2022

class Node():
    def __init__(self, value=None):
        self.next = None
        self.value = value


class LinkedList():
    def __init__(self, value=None):
        # how could I create a linked list with just a initializer?
        # if I give this an array how could I link it?
        self.node = self.create_list(value)
        # print(self.node.value)
        # print(self.node.next)

    def create_list(self, value):
        if type(value) == list:
            node = head_node = Node(value[0])
            #! node and head_node are referenced with the same pointer but only the "node" is worked on
            #! the head_node is still at the head

            for i in range(1, len(value)):
                node.next = Node(value[i])
                node = node.next
            node.next = None
            # how can I convert the node back to the head?
        else:
            node = Node(value)

        return head_node  # isn't this going to return the node at the last node?

    def print_list(self):
        current = self.node
        while current:
            print(current.value)
            current = current.next


def intersection(l1, l2):
    # find lenghts
    #! edge cases
    l1_length = 0
    l2_length = 0
    l1_current = l1
    l2_current = l2
    while l1_current:
        l1_length += 1
        l1_current = l1_current.next

    while l2_current:
        l2_length += 1
        l2_current = l2_current.next

    while l2 is not None and l1 is not None:
        if l2_length > l1_length:
            l2 = l2.next
            l2_length -= 1

        if l1_length > l2_length:
            l1 = l1.next
            l1_length -= 1
        print(l1, l2)
        if l1 == l2:
            return l1

        l1 = l1.next
        l2 = l2.next

    return None


node1 = Node([5, 2, 3, 2, 3, 1])
node2 = Node([9, 1, 3])
node_intersection = Node([5, 4, 3])

node1.next = node_intersection
node2.next = node_intersection

print(intersection(node1, node2))
