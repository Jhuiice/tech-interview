from collections import deque


class Node():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def bfs(root):
    if not root:
        return 0

    q = deque([root])
    collections_sum = 0

    while q:
        curr = q.pop()
        collections_sum += curr.val
        if curr.right:
            q.appendleft(curr.right)
        if curr.left:
            q.appendleft(curr.left)

    return collections_sum


def dfs(root):
    if not root:
        return 0

    value = root.val

    value += dfs(root.right)
    value += dfs(root.left)

    return value


a = Node(12)
b = Node(24)
c = Node(1)
d = Node(4)
e = Node(90)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(bfs(a))
print(dfs(a))
