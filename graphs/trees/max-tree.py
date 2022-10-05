# Definition for a binary tree node.
from collections import defaultdict, deque


class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def max_sub_tree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(root):
            if not root:
                return 0

            value = root.val

            value1 = dfs(root.left)
            value2 = dfs(root.right)

            value += max(value1, value2)

            return value

        return dfs(root)


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
print(sol.max_sub_tree(three))
