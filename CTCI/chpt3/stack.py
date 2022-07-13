class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None


# when implementing a stack the head is always the top. This will stop the error of return the None on the tail
class Stack():
    def __init__(self, value=None):
        self.node = Node(value)
        self.top = self.node

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

    def peek(self):
        if self.top == None:
            return "Stack is empty"
        return self.top.value

    def is_empty(self):
        return self.top == None


stack = Stack(1)
stack.push(2)
print(stack.peek())
print(stack.is_empty())
stack.pop()
stack.pop()

print(stack.pop())
print(stack.pop())
