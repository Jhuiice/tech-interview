from collections import deque


class Node():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def bfs(root, val):
    if not root:
        return False
    q = deque([root])

    while q:
        curr = q.pop()

        if curr.val == val:
            return True

        if curr.left:
            q.appendleft(curr.left)
        if curr.right:
            q.appendleft(curr.right)

    return False


# ? How do i make this break out of the stack? Force Quit a stack? when the val is equal to the wanted val
def dfs(root, val):
    if not root:
        return False

    if root.val == val:
        return True

    dfs(root.right, val)
    dfs(root.left, val)

    return False


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(bfs(a, 'a'))
print(bfs(a, 'r'))
print(dfs(a, 'a'))
print(dfs(a, 'r'))
