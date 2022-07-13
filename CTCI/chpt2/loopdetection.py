# # loop detection will check if there is a loop inside the linked list.
# # this problem will involve a runner
# # this will be a memory pull of my knowledge of linked lists
# # Date July 6th, 2022

# class Node():
#     def __init__(self, value=None):
#         self.next = None
#         self.value = value


# class LinkedList():
#     def __init__(self, value=None):
#         # how could I create a linked list with just a initializer?
#         # if I give this an array how could I link it?
#         self.node = self.create_list(value)
#         # print(self.node.value)
#         # print(self.node.next)

#     def create_list(self, value):
#         head_node = Node()
#         if type(value) == list:
#             node = head_node = Node(value[0])
#             #! node and head_node are referenced with the same pointer but only the "node" is worked on
#             #! the head_node is still at the head

#             for i in range(1, len(value)):
#                 node.next = Node(value[i])
#                 node = node.next
#             node.next = None
#             # how can I convert the node back to the head?
#             self.node = head_node
#         else:
#             self.node = Node(value)

#         return head_node  # isn't this going to return the node at the last node?

#     def print_list(self):
#         current = self.node
#         while current:
#             print(current.value)
#             current = current.next

#     def insert(self, value):
#         pass

#     def insert_before(self, node_value, new_value):
#         pass

#     def insert_after(self, node_value, new_value):
#         pass

#     def delete(self):
#         # uses the search methology but there are extra steps
#         self.node = self.node.next

#     def search(self, value):
#         current = self.node
#         while current != None:
#             if current.value == value:
#                 return True

#             current = current.next

#         return False

#     def reverse(self):
#         """Reverse literaly reverses the direcitons of the pointers on each node"""
#         # [1] => [2] => [3] => [4] => [5] => None
#         # None <= [1] <= [2] <= [3] <= [4] <= [5]
#         prev = None
#         current = reverse = self.node
#         # self.print_list()
#         # next = current.next
#         while current is not None:
#             next = current.next
#             current.next = prev
#             prev = current  # prev is the new linked list that starts at the head node of the reversed list
#             current = next  # this makes current None

#         self.node = prev
#         # it is only returning the tail node
#         # how do I do this?

# # TODO this problem below


# def loop_detection(l1):
#     # this is wrong if the loop has a circle it would never have a tail and never be none
#     while True:
#         walker = l1.next
#         runner = l1.next.next
#         if walker.value == runner.value:
#             return walker
#         print(l1.value)
#         l1 = l1.next

#     return None


# node = LinkedList([1, 2, 3])
# node.print_list()
# node1 = LinkedList([5])
# node2 = LinkedList([6])
# node3 = LinkedList([7])
# node4 = LinkedList([8])
# node5 = LinkedList([9])

# node1.print_list()
# node_placement = node1

#! use node.append() to add to the back of he list
# ? Can i use dequeu for this?
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# node5.next = node3

# # node1.print_list()
# node_placement.print_list()

# node_no_loop = LinkedList([1, 2, 3, 4, 5, 6])
# node_loop = LinkedList([1, 2, 3, 4, 5, 6, 3])

# print(node)
# print(node_no_loop.next.value)
# node_no_loop.print_list()
# loop_detection(node_loop)

# ! Start of the "askpython" circular code this is not my code

# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = self


# class CLL:
#     def __init__(self):
#         self.head = None
#         self.count = 0

#     def __repr__(self):
#         string = ""

#         if(self.head == None):
#             string += "Circular Linked List Empty"
#             return string

#         string += f"Circular Linked List:\n{self.head.data}"
#         temp = self.head.next
#         while(temp != self.head):
#             string += f" -> {temp.data}"
#             temp = temp.next
#         return string

#     def append(self, data):
#         self.insert(data, self.count)
#         return

#     def insert(self, data, index):
#         if (index > self.count) | (index < 0):
#             raise ValueError(
#                 f"Index out of range: {index}, size: {self.count}")

#         if self.head == None:
#             self.head = Node(data)
#             self.count += 1
#             return

#         temp = self.head
#         for _ in range(self.count - 1 if index - 1 == -1 else index - 1):
#             temp = temp.next

#         aftertemp = temp.next  # New node goes between temp and aftertemp
#         temp.next = Node(data)
#         temp.next.next = aftertemp
#         if(index == 0):
#             self.head = temp.next
#         self.count += 1
#         return

#     def remove(self, index):
#         if (index >= self.count) | (index < 0):
#             raise ValueError(
#                 f"Index out of range: {index}, size: {self.count}")

#         if self.count == 1:
#             self.head = None
#             self.count = 0
#             return

#         before = self.head
#         for _ in range(self.count - 1 if index - 1 == -1 else index - 1):
#             before = before.next
#         after = before.next.next

#         before.next = after
#         if(index == 0):
#             self.head = after
#         self.count -= 1
#         return

#     def index(self, data):
#         temp = self.head
#         for i in range(self.count):
#             if(temp.data == data):
#                 return i
#             temp = temp.next
#         return None

#     def size(self):
#         return self.count

#     def display(self):
#         print(self)


# nums = CLL()
# nums.append(1)
# nums.append(2)
# nums.append(3)
# nums.append(4)
# nums.append(5)
# nums.append(6)

# nums2 = CLL()
# nums2.append(5)
# nums2.append(9)

# nums.append(nums2)
# print("nums", nums)
# nums.display()

# this is the node class which has data and next
class Node:

    # Constructor to create  a new node
    def __init__(self, data):
        self.data = data
        self.next = None
# this is the actual circular linked list class which is made of Nodes


class CircularLinkedList:

    size = 0
    # size of the list

    # constructor
    def __init__(self):
        self.head = None
        self.tail = None

    # this inserts the node at the very front of the list
    def insertAtFront(self, node):

        if self.head is None:  # head is null
            node.next = self.head
            self.head = node
            self.tail = node
            self.tail.next = self.head

        else:  # if head is not null
            node.next = self.head
            self.head = node
            self.tail.next = self.head
        self.size += 1  # size increases

    # this is used to insert at the very bcak of th lisr
    def insertAtBack(self, node):

        # Case when list is empty
        if self.head is None:
            self.insertAtFront(node)

        else:
            node.next = self.head
            self.tail.next = node
            self.tail = node
            self.size += 1

    # this function does not fully work but should allow the user to insert at a certain index
    def insertAt(self, node, index):

        if self.head is None or index == 0:
            self.insertAtFront(node)
        elif index == self.size:
            self.insertAtBack(node)
        else:
            current_node = Node(None)
            if 0 < index < self.size:
                current_node = self.head.next
                position = 0

            while position < index - 1:
                position += 1
                current_node = current_node.next

            node = Node(node.data)
            current_node.next = node
            self.shiftToleft()

    # this shifts the list to the left  and is used when a certain node is inserted at a index
    def shiftToleft(self):
        temp = self.head
        if self.head is not None:
            while (True):
                if (temp.next == self.tail):
                    break
                temp = temp.next
            self.head = self.tail
            self.tail = temp

    # this function prints the list
    def print(self):
        print("The list contains : ")
        temp = self.head
        if self.head is not None:
            while (True):
                print(temp.data)
                temp = temp.next
                if (temp == self.head):
                    break


# Creating nodes to put into the list
list = CircularLinkedList()
for x in range(6):
    newNode = Node(x)
    list.insertAtBack(newNode)


node = Node(10)
list.insertAtFront(node)
list.shiftToleft()
# list.insertAt(node,2)
print("Following is the list ")
list.print()
print("Size of list is %d " % list.size)


def loop_detection(l1):
    # this is wrong if the loop has a circle it would never have a tail and never be none
    count = 0
    while count < 6:
        walker = l1.head.next
        runner = l1.head.next.next
        # if walker.value == runner.value:
        #     return walker
        print(l1.head.data, l1.head)
        count += 1
        l1.head = l1.head.next


# loop_detection(nums)
