# CTCI 4.4

# Check balanced
import math


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

    def check_height(self, value=0):
        height = value
        if self.parent != None:
            self = self.parent
            height = self.check_height(value + 1)
        return height

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

# implement a function to check if the binary tree is balanced
# ? what does balanced mean?
# the height of the two subtrees never differ by more than 1
# we can use depth first search to get each depth of a path
# then compare the depth of the mins and maxs of tree paths
# the brute force time complexity will take O(n)

# ! code from WilliamFiset Depth First search Algoithm youtube video

# function dfs(at):
#     if visited[at]: return
#     visited[at] = True

#     neighbors = graph[at]
#     for next in neighbors
#         dfs(next)

# start_node = 0
# dfs(start_node)


def dfs(tree, start):

    # what would I need to track the path of DFS?
    # colors?
    # visited array?
    # min and max for sure the dfs will return numbers if its being recursed and a true or false value
    # max - min > 1
    # implemented check height but i have to get the height of the bottom most nodes
    max_len = 0
    min_len = 0

    visited = [False] * tree.size
    prev = [None] * tree.size
    node = tree
    while False not in visited:

        if node not in visited:
            visited[start] = node

        if max_len - min_len > 1:
            return False

    return True


# def get_height(root):
#     if root == None:
#         return -1
#     return max(get_height(root.left), get_height(root.right)) + 1


# def is_balanced(root):
#     if root == None:
#         return True
#     height_diff = get_height(root.left) - get_height(root.right)
#     if math.floor(height_diff) > 1:
#         return False
#     else:
#         return is_balanced(root.left) and is_balanced(root.right)

# create a binary tree that is unbalanced

# ! NOTE TO SELF
# you can recurse a function to flow through a graph and check nodes
# just put the adjacent, left, or right node into the recusion and it will check

def check_height(root):
    if root == None:
        return -1

    left_height = check_height(root.left)
    if (left_height == None):
        return None
    right_height = check_height(root.right)
    if (right_height == None):
        return None

    if abs(left_height - right_height) > 1:
        return None
    else:
        return max(left_height, right_height) + 1


def is_balanced(root):
    return check_height != None


tree = TreeNode(6)
tree.insert_in_order(7)
tree.insert_in_order(8)
tree.insert_in_order(10)
tree.insert_in_order(12)
tree.insert_in_order(4)
tree.insert_in_order(5)

print(is_balanced(tree))
# print(tree.right.data)
# print(tree.left.data)
# print(tree.right.right.data)
# print(tree.right.right.right.data)
