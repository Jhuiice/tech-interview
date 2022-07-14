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
# ! If I am asked any type of find if the nodes are connected.
# ! My questions should involve
# ! What is the starting node?
# ! What are the data structures the graph is stored in? Adjaceny List, Matrix, LinkedList, Array, Dictionary
# * The only types of trees that nodes can be held in an array are complete binary trees


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
    # visited = [False] * n
    # nodes that corespond to the position of e
    # ? how do we construct the position of the nodes from e to s? keep track of their parents?
    # prev = [None] * n

    q = deque([tree])
    # q.appendleft(s)

    while len(q) != 0:
        # you cant use a for loop on a tree and its nodes you would need to use a while loop
        # i can run a for loop on the python library queue
        node = q.pop()
        print(node.data)
        if node.data == e:
            return True

        # but where does it stop?
        # * access points .size, .left, .right,
        if node.left:
            q.appendleft(node.left)
        if node.right:
            q.appendleft(node.right)

    return False


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


def bfsV2(graph, visited, start, end):
    visited.append(start)
    queue.append(start)
    while queue:  # queue will always have a node inside of it when it is searching
        s = queue.pop(0)
        print(s, end=' ')
        for neighbor in graph[s]:
            if neighbor == end:
                return True
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


# print(tree.data)
# print(solve(tree, 5, 9))

# ! this algorithm is wrong for the questions being asked
# I am supposed to see if two nodes connect on a directed graph not that if a node is present
# the below is a search algorithm for a binary tree
# im on the right path just not there yet
def solveV2(tree, e):

    q = deque([tree])

    # this algorithm will only work with binary trees
    # ? How would you solve this if the graph had more than 2 edges per vertex?
    # the data structure would be an array or a hash map
    # the approach would be the same but I would need to pull each hash key to get the values(nodes) and queue them up
    # would I still need to see which ones Ive visited or can I dequeue to be sufficient when I pull the node?
    # I think I would need to add to visited to make sure I dont deque too soon
    while len(q) != 0:
        node = q.pop()
        print(node.data)
        if node.data == e:
            return True
        # * on second thought I think this is correct although if this was not a tree I would need to see if the nodes
        # * were visited so I dont add them back to the queue and make an infinite loop
        if node.left:
            q.appendleft(node.left)
        if node.right:
            q.appendleft(node.right)

    return False


tree2 = TreeNode(7)
tree2.insert_in_order(8)
tree2.insert_in_order(9)
tree2.insert_in_order(10)
tree2.insert_in_order(11)
tree2.insert_in_order(12)
tree2.insert_in_order(13)
tree2.insert_in_order(14)
tree2.insert_in_order(1)


# print(solveV2(tree2, 14))

def solveV3(tree3, start, end):
    visited = [False] * tree3.size
    prev = [None] * tree3.size

    q = deque([tree3])
    i = 0  # since it is a binary tree the root is 0
    while len(q) != 0:
        node = q.pop()
        if node not in visited:
            # ? how would I keep track of the index? n?
            visited[i] = node
            # ? are values coming out of prev and going back in per node visited?
            prev[i] = node

        q.appendleft(node.left)
        q.appendleft(node.right)
