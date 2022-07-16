# CTCI 4.9
# BST Sequeunce

# print an array of the order of the binary search tree and how it was intiated
# * I can traverse the tree and add nodes at depth from left to right
# * this would be a combination of a depth first search and a breadth first search
# * I would traverse the tree from the left or right first children nodes and then
# * traverse each subtree at breadth level and the combination of node values can
# * be inserted every other but the tree is root = 2 left = 1 right = 3

# ? How would I implement this?
# what would the time complexity be? O(N) it would traverse through every node multiple times
# the tree is root = 2, left = 1, right = 3

# time complexity is O(n * 2)
# it works with height is 2 lets see if it works with a larger tree

from collections import deque


def bst_sequence(root):
    if root.left == None and root.right == None:
        return [root.data]
    build_arrs = []
    # root will always be index 0
    # the for loop will run through with n = h
    # for i in range(len(root.size)):
    # this will not change the access I have
    # * I Could brute force this and just return the array sequence but how would I code this?
    # ? do I know all traversal methods? could I call a traversal method from left and from right as perorder traversal?
    arr_left = []
    arr_right = []
    build_arrs.append(preorder_traversal_left(root, arr_left))
    build_arrs.append(preorder_traversal_right(root, arr_right))

    return build_arrs


def preorder_traversal_left(root, arr):
    if root:
        arr.append(root.data)
        preorder_traversal_left(root.left, arr)
        preorder_traversal_left(root.right, arr)

    return arr


def preorder_traversal_right(root, arr):
    if root:
        arr.append(root.data)
        preorder_traversal_right(root.right, arr)
        preorder_traversal_right(root.left, arr)

    return arr


# class Tree():
#     def __init__(self, data=None):
#         self.data = data
#         self.right = None
#         self.left = None
#         self.parent = None
#         self.size = 1 if data else 0


# tree = Tree(2)
# tree.left = Tree(1)
# tree.left.parent = tree
# tree.right = Tree(3)
# tree.right.parent = tree
# tree.size = 2

# print(bst_sequence(tree))

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

# * for a bigger tree
# ? could I implement a method to use breadth first search and create a linkedlist for each depth to do this?
# ? OR i could use breadth first search and create permutations of each level. This would take O(k^2 + n) k is equeal to
# ? number of nodes per depth or 2^(h-1) - (num of empty children) if the level is full
# ! I must change the bst_sequence function. Right now it only has access to two arrs
# ! the above bst_sequence function will not work for larger trees. It would be imcomplete
# I will try that if this does not work using preorder DFS


tree = TreeNode(50)
tree.insert_in_order(20)
tree.insert_in_order(60)
tree.insert_in_order(10)
tree.insert_in_order(25)
tree.insert_in_order(70)
tree.insert_in_order(5)
tree.insert_in_order(15)
tree.insert_in_order(65)
tree.insert_in_order(80)


def bst_sequence_2(root):
    q = deque([root])

    while len(q) != 0:
        node = q.pop()

        if node.left:
            q.appendleft(node.left)

        if node.right:
            q.apenndright(node.right)

        #! if I do this method I have to keep track of the depth of the tree. If the depths are not complete than this will not work. This method would only work for complete or true binary trees


print(bst_sequence(tree))

# CTCI Code


class LinkedList():
    def __init__(self, data=None):
        self.data = data
        self.next = None


def all_sequence(node):
    result = list(LinkedList())

    if node.data == None:
        return result

    prefix = LinkedList()
    prefix.data = node.data

    left_seq = all_sequence(node.left)
    right_seq = all_sequence(node.right)

    while left_seq is not None:
        while right_seq is not None:
            weaved = [LinkedList()]
            weave_lists(left_seq, right_seq, weaved, prefix)
            result.add_all(weaved)
            right_seq = right_seq.next

        left_seq = left_seq.next


def weave_lists(first, second, results, prefix):
    if first.size() == 0 or second.size() == 0:
        # I do not have the linkedlist class they are using so I dont know how to implement this
        result = prefix.clone()
        result.add_all(first)
        result.add_all(second)
        results.append(result)
        return

    head_first = first.remove_first()
    prefix.add_last(head_first)
    weave_lists(first, second, results, prefix)
    prefix.remove_last()
    second.add_first(head_first)

    head_second = second.remove_first()
    prefix.add_last(head_second)
    weave_lists(first, second, results, prefix)
    prefix.remove_last()
    second.add_first(head_second)
