from collections import deque
import random


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

# ? Route between Noeds: given a directed graph and two nodes (S and E), design an alogirthm to find out whether
# ? there is a route from S to E

# * My first thought is this will take O(n) time. The algorithm will be an implementation of BFS or BDS
# * BFS can scan more neighbor nodes faster and that would be ideal to finding the Node we are looking for
# * for this problem I will need a data structure to hold the nodes I have visited and a data structure to
# * contruct the path of the nodes from S to E this I will do backwards after I have found the Node E
# * I will have to reverse the list of nodes it took to get to the Node S.
# * BFS will be used with a queue so I will use the deque data structure from the Collections libary
# ? Another question I should have asked before attempting this problem is
# ? How is the graph represented? adjavency list or a adjaceny matrix or something different


tree = TreeNode(5)
tree.insert_in_order(6)
tree.insert_in_order(7)
tree.insert_in_order(8)
tree.insert_in_order(1)
tree.insert_in_order(2)
tree.insert_in_order(3)
tree.insert_in_order(4)
tree.insert_in_order(5)
tree.insert_in_order(9)

# ? do we have the size of the tree? with the data structure of the binary tree I am using there is a size attribute
n = tree.size
s = tree.data
e = 7


def solve(tree, s, e):
    # nodes list that is the size of the amount of nodes in the tree
    nodes = [False] * n
    # nodes that corespond to the position of e
    # ? how do we construct the position of the nodes from e to s? keep track of their parents?
    prev = [None] * n

    q = deque([])
    q.appendleft(s)

    while len(q) != 0:
        pass


def bfs(tree, s, e):

    # there are white, grey, and black nodes
    # we can insert the data into the nodes if neccessary
    # we have to check through all nodes first at s + k then s + (k + 1)
    # we insert into the queue new nodes and dequeue nodes when we have visited all of their children nodes
    solve(tree, e, s)


# print(tree.left.data, tree.right.data)
# while tree != None:
#     left = tree.left
#     right = tree.right

#! second attempt with a differnt starting graph data structure
# this graph is from grakking the coding interview breadth depth first example
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []
queue = []


def bfs(graph, visited, node, end):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s, end=' ')
        for neighbor in graph[s]:
            if neighbor == end:
                return True
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


bfs(graph, visited, 2)
