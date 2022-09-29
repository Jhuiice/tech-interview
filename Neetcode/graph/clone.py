from collections import deque


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node):
    """
    :type node: Node
    :rtype: Node
    """
#     if not node:
#         return []
#     if len(node.neighbors) == 0:
#         return Node(node.val)
#     queue = deque([node])
#     # queue = deque([node.neighbor[0]])
#     # copy = Node(node.val, [Node(neighbor.val) for neighbor in node.neighbors])
#     # dummy = copy
#     visited = set()
#     while len(queue) > 0:
#         current = queue.pop()
#         if current in visited:
#             continue
#         visited.add(current)
#         new_node = Node(current.val)  # creation of the new node
# # deep clone need to recreate the object
#         for neighbor in current.neighbors:
#             new_node.neighbors.append(Node(neighbor.val).neighbors.append(new_node))
#         for neighbor in new_node.neighbors:  # * not optimized lets see if it works
#             if neighbor not in new_node:
#                 neighbor.neighbors.append(new_node)

#     if node.val == 1:
#         return node
#     for neighbor in no
#     return dummy

    old_to_new = {}

    def dfs(node):
        # visited task
        if node in old_to_new:
            return old_to_new[node]

        copy = Node(node.val)
        # key is node value is a copy of the node
        old_to_new[node] = copy

        for neighbor in node.neighbors:
            copy.neighbors.append((dfs(neighbor)))

        return copy

    return dfs(node) if node else []


adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]
# Output: [[2, 4], [1, 3], [2, 4], [1, 3]]

print(cloneGraph(node1))


def cloneBFS(node):
    if not node:
        return None

    q, clones = deque([node]), {node.val: Node(node.val, [])}

    while q:
        cur = q.popleft()
        cur_clone = clones[cur.val]

        for ngbr in cur.neighbors:
            if ngbr.val not in clones:
                clones[ngbr.val] = Node(ngbr.val, [])
                q.append(ngbr)
                # how do i append neighbors????????
            cur_clone.neighbors.append(clones[ngbr.val])

    return clones[node.val]


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        q, clones = deque([node]), {node.val: Node(node.val, [])}
        while q:
            cur = q.popleft()
            cur_clone = clones[cur.val]

            for ngbr in cur.neighbors:
                if ngbr.val not in clones:
                    clones[ngbr.val] = Node(ngbr.val, [])
                    q.append(ngbr)

                cur_clone.neighbors.append(clones[ngbr.val])

        return clones[node.val]
