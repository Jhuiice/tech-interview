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

    def insert(self, value):
        pass

    def insert_before(self, node_value, new_value):
        pass

    def insert_after(self, node_value, new_value):
        pass

    def delete(self):
        # uses the search methology but there are extra steps
        self.node = self.node.next

    def search(self, value):
        current = self.node
        while current != None:
            if current.value == value:
                return True

            current = current.next

        return False

    def reverse(self):
        """Reverse literaly reverses the direcitons of the pointers on each node"""
        # [1] => [2] => [3] => [4] => [5] => None
        # None <= [1] <= [2] <= [3] <= [4] <= [5]
        prev = None
        current = reverse = self.node
        # self.print_list()
        # next = current.next
        while current is not None:
            next = current.next
            current.next = prev
            prev = current  # prev is the new linked list that starts at the head node of the reversed list
            current = next  # this makes current None

        self.node = prev
        # it is only returning the tail node
        # how do I do this?


# this initializes it but does not start it at its head. How do I do that?
# how would I send the linked-list back to the head?
node = LinkedList([1, 2, 3, 4])
# print("node search 2 ", node.search(2))
# node.print_list()
# print("node serach 2 ", node.search(2))
# print("node serach 4 ", node.search(4))
# node.delete()
# node.print_list()
# node.delete()
# node.print_list()
# print("right after print_list")
# # new_node.delete(1)
# # new_node.print_list()

node_2 = LinkedList([1, 2, 3, 4, 5])
# print(node_2.search(4))
node_2.print_list()
# node_2.reverse()
# node_2.print_list()
