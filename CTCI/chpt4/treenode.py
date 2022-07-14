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


# tree = TreeNode(4)
# tree.insert_in_order(3)
# tree.insert_in_order(4)
# tree.insert_in_order(5)
# tree.insert_in_order(6)
# root = tree.data
# root_left = tree.left.data
# root_right = tree.right.data
# root_p = tree.parent
# root_left_p = tree.left.parent.data
# root_right_p = tree.right.parent.data
# print(root, root_left, root_right)
# print(root_p, root_left_p, root_right_p)
# # print(tree.find(6))
# print("root", tree.data)
# print("Left child of root", tree.left.data)
# print("Left child parent of root", tree.left.parent)
# print("Right child", tree.right.data)
# print("Right child parent data from root", tree.right.parent)
# print(tree.right.right.parent.data)
# print(tree.right.left.parent.data)

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
tree = TreeNode(arr[5])

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
