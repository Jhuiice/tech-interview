# Memory Pull of July 18th

# linked lists
class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self, data=None):
        self.head = Node(data)
        self.tail = None

    def append(self, data):
        if data == None:
            return None

        head = self.head
        self.head = Node(data)
        self.head.next = head

    def add_in_front(self, node_data, data):
        pass

    def search(self, data):
        head = self.head
        while head is not None:
            if data == head.data:
                return True
            head = head.next
        return False

    def delete(self, data):
        if self.head == self.tail:
            return "Underflow"

        if self.head.data == data:
            self.head = self.head.next
            return data

        head = self.head
        next = head.next

        while head is not None and next is not None:
            if data == next.data:
                head.next = head.next.next
                return data
            head = head.next
            next = next.next

        return False

    def pop(self):
        pass

    def print_list(self):
        head = self.head
        while head is not None:
            print(head.data)
            head = head.next


ll = LinkedList(4)
# print(ll.delete(4))
print(ll.append(5))
print(ll.append(6))
print(ll.append(7))
print(ll.append(8))
# print(ll.delete(6))
ll.print_list()


# stacks
# pop and append always take from the head in O(1)
# search will be O(n)
# queues
# append is O(1) pop is always O(n) search is O(n)

# binary trees
# time complexity is O(lg(n))

# graphs

# heaps
# min heaps and max heaps min heaps have lowest value as the root maxheaps have largest node value at root
# These heaps are designed where all left <= root <= right like a binary search tree. But they are always
# heapified when new elements are added and deleted comparing and relocating

# sorting
# quick sort
# merge sort

# hash maps
# dictionaries

# arrays and matrices and strings
# these

