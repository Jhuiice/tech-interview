# CTCI 4.8
# first common ancestory

# find the first common ancestor of two nodes in a binary tree. So nodes above the parents are the ancestory
# find the first coomon one

# * idea: we can store the value of the grandparent node in each node upon creation?
# psuedcode would be
# root.ancestor is none
# child1.ancestor is none
# grandchild.ancestor is root this would allow the grandchilds children access to the ancestor
# ! the interviewer might not let us do this
# ? what if we had no link to our parent?
# ? How are we going to store the nodes to compare.
# The first common ancestor could be the root of a tree with height 6 and its furthest child.
# ? How would we go about this problem?
# ? whats considered an ancestor? the parent or the parents parent?

#               8
#             /  \
#            5    9
#          /  \  /  \
#         4   6 8   10

# first common ancestor of 4 and 6 is 5
# first common ancestor of 8 and 10 is 9
# first common ancestor of 4 and 10 is 8
# this problem does not neessarily use a binary search tree

# brute force I am going to use another data structure to calculate the parents of the children
# i can use a sequence of BFS to find all the children of the nodes at hand and put them into an array?
# i would use DFS to find the first common ancestor?

# What are the characterisics of a binary tree

from collections import deque

# TODO come back to this problem


class Tree():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def insert_into(self, value):
        if value <= self.data:
            if self.left == None:
                self.insert_left(Tree(value))
            else:
                self.left.insert_into(value)

        else:
            if self.right == None:
                self.insert_right(Tree(value))
            else:
                self.right.insert_into(value)

    def insert_left(self, left):
        if self.left == None:
            self.left = left
            left.parent = self

    def insert_right(self, right):
        if self.right == None:
            self.right = right
            right.parent = self


def first_common_ancestor(root, node1, node2):
    if not root.left and not root.right:
        return None
    q = deque(root)

    while len(q) != 0:
        node = q.pop()
        parent = node
        if node.left:
            q.appendleft(node.left)
        if node.right:
            q.appendleft(node.right)
