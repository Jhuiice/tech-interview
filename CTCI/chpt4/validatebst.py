# CTCI 4.5
# validate BST

# implement a function to check if a binary tree is a binary tree
# what makes up a binary tree? what are it characteristics?
# parents can only have 1-2 children no more
# left.data <= right.data < parent.data
# no node on the left can be larger than the parent node

# if the tree was represented from a hasm map
# if the len of the list of a key is greater than 2 than return false

# if data was given in a matrix no node could have more than 2 intersections
# and no node could intersect with itsself

# if the data was given in a adjaceny list the list could not be longer than 2 nodes for each list

# brute force time complextiy is O(n)
# we must check all nodes in a fashion to see if they meet the criterias

# i will use breadth first search on the binary tree
from collections import deque


class BST():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    # def insert_left(self, left):
    #     if self.left == None:
    #         self.left = left

    # def insert_right(self, right):
    #     if self.right == None:
    #         self.right = right


non_bst = BST(3)
non_bst.left = BST(4)
non_bst.right = BST(2)

non_bst2 = BST(5)
non_bst2.left = BST(4)
non_bst2.left.right = BST(8)

good_bst = BST(6)
good_bst.left = BST(4)
good_bst.right = BST(7)
good_bst.left.left = BST(2)
good_bst.left.right = BST(3)

# this is not optimized for how many conditionals I have
# ! whoops... optimized code below


def validate_bst(graph):
    if graph.data == None:
        return False

    root_data = graph.data
    # validate based on left and right side
    node_left = graph.left
    node_right = graph.right
    if node_left:
        if node_left.data > root_data:
            return False
    if node_right:
        if node_left.data > node_right.data:
            return False
    if node_left and node_right:
        if node_left.data > node_left.data:
            return False

    left_q = deque([node_left])
    right_q = deque([node_right])

    while len(left_q) != 0:
        node = left_q.pop()
        # print(node)

        if node.left:
            if node.parent:
                if node.left.data > node.parent.data:
                    return False
            if node.left.data > root_data:
                return False
            left_q.appendleft(node.left)

        if node.right:
            if node.parent:
                if node.right.data > node.parent.data:
                    return False
            if node.right.data > root_data:
                return False
            left_q.appendleft(node.right)

        if node.right and node.left:
            if node.left.data > node.right.data:
                return False

    while len(right_q) != 0:
        node = right_q.pop()

        if node.left:
            if node.parent:
                if node.left.data < node.parent.data or node.left.data < root_data:
                    return False
            left_q.appendleft(node.left)

        if node.right:
            if node.parent:
                if node.right.data < node.parent.data or node.right.data < root_data:
                    return False
            left_q.appendleft(node.right)

        if node.right and node.left:
            if node.left > node.right:
                return False
    return True


# print(validate_bst(non_bst))
# print(validate_bst(non_bst2))
# print(validate_bst(good_bst))

global last_printed
last_printed = None


def check_bst(node):
    if node == None:
        return True
    if not check_bst(node.left):
        return False
    if last_printed != None and node.data < last_printed:
        return False
    last_printed = node.data

    if not check_bst(node.right):
        return False

    return True


# I will say this works but I have no confirmation. My scope is being weird
print(check_bst(non_bst))
print(check_bst(non_bst2))
print(check_bst(good_bst))
