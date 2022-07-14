#
# ? CTCI 4.2
# The structure of a binary search tree is smallest elements end up in the left most leaf
# the leafs are added from left to right regardless of state
# if the numeber is larger than the root add it to the right side
# if the added number is less than the root add it to the left side
# for this I can use a bottom up approach or split the array in half and use the
# middle of the array as a my starting node and start with a top down approach
# this graph has to be minimal height for the question and its under my discretion how its handled
# each addition to the graph would take O(lg(n)) time to appropriatley place the nodes
# O(lg(n)) becuase the route is cut in half everytime the node goes to a higher height

class BinarySearchTree():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.size = 1 if data else 0

    # keep track if the left or right node is None or no
    def insert_in_order(self, data):
        if data <= self.data:
            if self.left == None:
                self.insert_left(BinarySearchTree(data))
            else:
                self.left.insert_in_order(data)
        else:
            if self.right == None:
                self.insert_right(BinarySearchTree(data))
            else:
                self.right.insert_in_order(data)

        self.size += 1

        # needs some form of recursion right here

    def insert_left(self, left_node):
        self.left = left_node
        if left_node != None:  # this wont hold true for the root node ? How can I make that happen?
            left_node.parent = self

    def insert_right(self, right_node):
        self.right = right_node
        if right_node != None:  # can change this type check if we do the type check in the insert in order
            right_node.parent = self


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
tree = BinarySearchTree(arr[5])

# nodes are not sinking into list they are just getting replaced
# * the insertion of nodes always starts with the root for top down approach
# * to minimize the tree I can use 2 for loops on starting from the center and one from the beggining
print(arr[len(arr)//2])
for i in range(len(arr)//2, len(arr)):
    tree.insert_in_order(arr[i])
for j in range(len(arr)//2-1, -1, -1):
    tree.insert_in_order(arr[j])
print(tree.data)
print(tree.right.data)
print(tree.right.right.data)
print(tree.right.right.right.data)
print("left", tree.left.data)
print(tree.left.left.data)
print(tree.left.left.left.data)
