# class List():
#     def __init__(self, value=None):
#         self.next = None
#         self.value = value
#         self.prev = None

#     def head(self):
#         if self.value != None:
#             while self.prev != None:
#                 self.prev = self.prev.prev

# * requires to have a node class and a linked list class

from collections import deque


class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self, data=None):
        self.head = Node(data)
        self.tail = None


# * must assign nodes into the linked list
llist = LinkedList(1)
print(llist.head.data)

# attributes of linked-lists
# insert O(1)
# deleteHead O(1)
# deleteTail O(n)
# deleteSpecific O(n)
# insertBehind O(n)
# insertAhead O(n)
# insertHead O(1)
# insertTail O(n)

# benefits of linked lists?
# Can store mappings and multiple forms of nodes in the linked list.
# Pointer access
# Downfalls of linked lists?
# The downfalls of linked lists is they use more memory allocations than a normal list,
# they cannot be accessed O(1) with an index like a list

# Structure of a linked list
# Doubly linked => [[prev][data][next]] => [[head]<=>[x1]<=>[x2]<=>[tail]<=>[null]]
# in the sense of head.next.prev = x x.next = head.next
# head points to next and then takes the pointer for the next and points with the "prev" pointer to x
# this is a way to remove the head and replace it with a new object value


# * collections
# ? You can access deque structure as a list

def queue(l):
    llist = deque(l)


class Queue():
    def __init__(self, data):
        self.queue = deque(data)

    def insert(self, value):
        self.queue


queue(["a", "b", "c"])
