# Definition for a binary tree node.
from collections import defaultdict, deque


class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        order = defaultdict(list)
        q = deque([(root, 1)])
        children = []
        level = 1

        while q:
            cur, level = q.pop()
            print(level)
            order[level].append(cur.val)
            if cur.left:
                q.appendleft((cur.left, level+1))
            if cur.right:
                q.appendleft((cur.right, level+1))

        ans = []
        for level in order.keys():
            ans.append(order[level])

        return ans


three = Node(3)
nine = Node(9)
twenty = Node(20)
fifteen = Node(15)
seven = Node(7)

three.left = nine
three.right = twenty
twenty.left = fifteen
twenty.right = seven

one = Node(1)

none = []

sol = Solution()
print(sol.levelOrder(three))
print(sol.levelOrder(one))
print(sol.levelOrder(none))
