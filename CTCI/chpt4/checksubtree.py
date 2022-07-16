# CTCI 4.10
# check subtree

# you will be given t1 and t2 t1 is much much larger than t2.
# a subtree is determined if a starting node and all its successors are the same
# ie you can chop off the subtree at the node and subtree of t1 == t2
# t1 and t2. That t2 is a subtree of t1

# * The way i think of going about this is to traverse the tree with DFS
# * check each node and check if its identical to the root of t2
# * then traverse both trees with the same algorithms and check if
# * each node traversed is identical until you result in the ending nodes.
# * to determing the ending nodes of t2. The leafs of t1 and t2 should be identical


# ? can i use preorder DFS to compare nodes?
# ? how would i do this synchronously?
# ? this would be O(n)

# ? another method could be traversing the trees with breadthfirst search
# ? creating an array for each and then using sliding glass window to compare the subset
# ? of t2 in t1? that would be O(n1 + n2 + n1) and space complexity is increased to O(n1 + n2)

# ! i can use DFS and create a string of each node and then see if t2 is in t1


def check_subtree(t1, t2):
    def preorder_traversal_sync(t1, t2):
        if t1:
            if t1.data == t2.data:
                print("t1 == t2")
                preorder_traversal_sync(t1.left, t2.left)
                preorder_traversal_sync(t1.right, t2.right)
                return True
            else:
                return None

    # result = False

    def preorder_traversal(root):
        if root:
            if root.data == t2.data:
                result = preorder_traversal_sync(root, t2)
                # this equals true but then
                print("result inside comparison", result)
            else:
                print(root.data)
                preorder_traversal(root.left)
                preorder_traversal(root.right)

            return result

    return preorder_traversal(t1)


class Tree():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


t1 = Tree(8)
t1.right = Tree(80)
t1.left = Tree(3)
t1.right.left = Tree(11)
t1.right.right = Tree(10)
t1.left.left = Tree(2)
t1.left.right = Tree(4)

t2 = Tree(80)
t2.left = Tree(11)
t2.right = Tree(10)

# * I can accuratley compare and get the correct comparisons but I can't seem to figure out how to return the boolean value
# print(check_subtree(t1, t2))

# im going to use traversal to get a string list

# * had to get help from the CTCI solution
# * remember how to join and join only takes others strings inside lists


def check_subtree_v2(t1, t2):
    string1 = []
    string2 = []
    preorder_traversal(t1, string1)
    preorder_traversal(t2, string2)

    string1 = "".join(string1)
    string2 = "".join(string2)

    print(string1, string2)
    if string2 in string1:
        return True
    else:
        return False

# ? How do i add to a subtring from recusion? the same as adding


def preorder_traversal(root, sb):
    if root == None:
        return None

    sb.append(str(root.data))
    preorder_traversal(root.left, sb)
    preorder_traversal(root.right, sb)


print(check_subtree_v2(t1, t2))
