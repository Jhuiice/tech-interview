# CTCI 4.11
# Random node

# design and implement a method that receives a random node from a binary search tree

# ? how can i approach this problem?
# I can create a list of the node values and input a data field into the root node?
# Then from there when i call get random node it would take the length of the list
# use random.randint(len(list_tree_nodes)) and then search through the tree node to
# pull that value? random.randint() isn't entirely random
# can I do this without increasing the space complexity?

# given the size of the tree I can take a random number from that traverse through the
# tree with a random ness of in-order, pre-order, and post-order traversal??

# ! design a class with insert, delete, find, and randomnode
# ! this is your own custom class so you can implememnt whichever you want


import random


def random_node(root):
    pass


def in_order(root, count):
    if root == None:
        return count
    if count == 0:
        return root.data
    count -= 1
    count = in_order(root.left, count)
    count = in_order(root.right, count)

    return count


# def pre_order(root, count):
#     if root:
#         if count == 0:
#             return root.data
#         in_order(root.left)
#         in_order(root.right)


# def in_order(root, count):
#     if root:
#         if count == 0:
#             return root.data
#         in_order(root.left)
#         in_order(root.right)


class Tree():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.size = 7


t1 = Tree(8)
t1.right = Tree(80)
t1.left = Tree(3)
t1.right.left = Tree(11)
t1.right.right = Tree(10)
t1.left.left = Tree(2)
t1.left.right = Tree(4)

# print(in_order(t1, random.randint(1, 7)))
print(in_order(t1, 1))
