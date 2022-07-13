# sort stack

from urllib.parse import non_hierarchical


class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None


# when implementing a stack the head is always the top. This will stop the error of return the None on the tail
class Stack():
    def __init__(self, value=None):
        self.node = Node(value)
        self.top = self.node
        self.size = 1 if value else 0

    def pop(self):
        if self.top == None:
            return "Empty Stack"
        item = self.top.value
        self.top = self.top.next
        return item

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def peek(self):
        if self.top == None:
            return "Stack is empty"
        return self.top.value

    def is_empty(self):
        return self.top == None


# at the end of this the smallest item will end up at the head of the stack
# compare the values of the two stacks if the value of one is less than the other send it to the
# smaller stack
def sort_stack(s):

    r = Stack()
    while not s.is_empty():
        tmp = s.pop()
        # print(r.is_empty())
        while not r.is_empty() and r.peek() > tmp:
            s.push(r.pop())
        r.push(tmp)

    while not r.is_empty():
        # * will implement a new stack backwards this is key for stack problems
        s.push(r.pop())


stack = Stack(1)
for i in range(4):
    stack.push(i + 2)

sort_stack(stack)

print(stack.peek())
