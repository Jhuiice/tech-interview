from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree1 = TreeNode(0, TreeNode(1), TreeNode(2))
tree2 = TreeNode(0, TreeNode(1), TreeNode(2))

tree3 = TreeNode(1, TreeNode(2), TreeNode(1))
tree4 = TreeNode(1, TreeNode(1), TreeNode(4))


def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
#         Can create two data structures and compare them
#         Or compare at each interval
#         What are the edge cases? 1 node

    # root checks for edge cases
    if not (p and q):
        return True
    if (p and q) and p.val == q.val:
        return isSameTree(q.left, p.left) and isSameTree(q.right, p.right)
    else:
        return False


print(isSameTree(tree1, tree2))  # true
print(isSameTree(tree1, tree3))  # false
