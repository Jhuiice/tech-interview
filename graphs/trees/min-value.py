# Definition for a binary tree node.
from collections import defaultdict, deque


class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def min_value(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        q = deque([root])
        min_value = float('inf')

        while q:
            cur = q.pop()
            if cur.val < min_value:
                min_value = cur.val

            if cur.left:
                q.appendleft(cur.left)
            if cur.right:
                q.appendleft(cur.right)

        return min_value


three = Node(3)
nine = Node(9)
twenty = Node(20)
fifteen = Node(15)
seven = Node(7)
one = Node(1)

three.left = nine
three.right = twenty
twenty.left = fifteen
twenty.right = seven
seven.left = one

none = []

sol = Solution()
print(sol.min_value(three))
