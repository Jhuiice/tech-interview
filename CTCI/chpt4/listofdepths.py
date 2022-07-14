# CTCI 4.3

# list of depths
from collections import deque
from this import d
# given a binary tree create a linked list at each depth


class TreeNode():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.size = 1 if data else 0

    def insert_in_order(self, data):
        if data <= self.data:
            if self.left == None:
                self.set_left_child(TreeNode(data))
            else:
                self.left.insert_in_order(data)
        else:
            if self.right == None:
                self.set_right_child(TreeNode(data))
            else:
                self.right.insert_in_order(data)

        self.size += 1

    def size(self):
        return self.size

    def find(self, data):
        if data == self.data:
            return self.data
        elif data <= self.data:
            return self.left.find(data) if self.left != None else None
        elif data > self.data:
            return self.right.find(data) if self.right != None else None
        return None

    def set_left_child(self, left):
        self.left = left
        if left != None:
            left.parent = self

    def set_right_child(self, right):
        self.right = right
        if right != None:
            right.parent = self


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
tree = TreeNode(arr[6])

for i in range(len(arr)//2+1, len(arr)):
    tree.insert_in_order(arr[i])
for j in range(len(arr)//2-1, -1, -1):
    tree.insert_in_order(arr[j])

# print("tree root", tree.data)


class LinkedList():
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def insert_into(self, value):
        if self.next == None:
            self.next = LinkedList(value)
        else:
            self.next.insert_into(value)

    def print_list(self):
        while self is not None:
            print(self.data)
            self = self.next


# breadth first search and sync to a linked list
# each depth has a deterministic value of nodes
# root is 1
# 2nd level is 2
# 3rd level is 4
# 4th level is 8
# the number of nodes at each depth is (n-1)^2
# print(tree.data)


def create_linked_lists(tree):
    q = deque([tree])

    if len(q) == 0:
        return False
    depth = 0
    node_count = 0
    ll = LinkedList()
    ll_list = []

    # temp = LinkedList()
    i = 0
    # since the tree is a binary tree I can be sure all nodes are being visited with the queue
    while len(q) != 0:
        # get the current node
        node = q.pop()
        # print(q)
        # print(i, node.data)
        i += 1
        # temp.insert_into(node.data)
        # # check edge case to see if node is root root only has one node per level
        # if node.data == tree.data:
        #     # print("inside")
        #     continue

        # check to see if ll is initialized
        if ll.data == None:
            # print("made a new list")
            ll = LinkedList(node.data)
            # pass by reference so any change will go to the one in the list
            ll_list.append(ll)
            depth += 1
        else:
            ll.insert_into(node.data)

        # increases count of nodes once nodes are linked
        node_count += 1
        # print(node_count)
        # append to queue if nodes has children
        if node.left != None:
            q.appendleft(node.left)
        if node.right != None:
            q.appendleft(node.right)

        # resets linked list when node_count
        if ((depth - 1)**2 == node_count and (depth - 1)**2 % 2 == 0) or depth == 1:
            # print((depth - 1) ** 2, node_count)
            # print("inside if", node.data)
            ll = LinkedList()
            # depth += 1

        # print(depth, node_count)

    return ll_list


temp = create_linked_lists(tree)

# print(temp[0].print_list())
# print(temp[1].print_list())
# print(temp[2].print_list())
# print(temp[3].print_list())
