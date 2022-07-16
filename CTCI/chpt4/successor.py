# CTCU 4.6

# successor

# find the next node if the next node has access to its parent but not parent to child
# wouldnt we need to start at the ending node ?
# if we are given a child node we cnas say child.parent.next = child
# but this would only take you so far

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


# TODO Learn more about in-order traversal
# * depth first search uses stacks with pre-order/in-order/post-order traverals
# NOTE There are probably more ways of traversing with depth first search


def in_order_traversal(root):
    if not root:
        return None
    # print(root.data) #! uncomment and this is preorder traversal
    in_order_traversal(root.left)
    print(root.data)  # in order is when the root.data is accessed
    # in_order_traversal(root)
    in_order_traversal(root.right)
    # print(root.data) #! uncomment and this is postorder traversal


def in_order_success(node):
    if node == None:
        return None

    if node.right != None:
        return left_most_child(node.left)
    else:
        q = node
        x = q.parent

        while (x != None and x.left != q):
            q = x
            x = x.parent

        return x


def left_most_child(node):
    if (node == None):
        return None
    while node.left != None:
        node = node.left

    return node


# in_order_traversal(tree)
print(in_order_success(tree).data)
