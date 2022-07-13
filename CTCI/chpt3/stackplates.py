
# ? whats the capacity of the stacks?
# ? must keep track of length of stacks
# ? do I need another data structure, Node? Stack?
# ? do i use a hash map for this problem? Would that add in more unneccisary dynamic?
# ? do i need to use a stack object to implement this?

class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None


# class SetOfStacks():
#     def __init__(self, value=None):
#         self.limit = 5
#         self.capacity = 0
#         # * there will be multiple tops this will not work
#         self.top = Node(value)
#         self.nodes = {0: {"capacity": 1 if value else 0,
#                           "node": Node(value)}}  # ! use an array
#         self.stacks = 0

#     def push(self, value):
#         capacity = self.nodes[self.stacks]["capacity"]
#         if capacity > 5:
#             self.stacks += 1
#             self.nodes[self.stacks] = {"capacity": 1, "node": Node(value)}

#         node = self.nodes[self.stacks]["node"]

#         self.top = node
#         node.top.next = top
#         node.top = Node(value)

#         # top = self.top
#         # self.top = Node(value)
#         # self.top.next = top

#     def pop(self):
#         # node = self.nodes[stack]["node"]
#         node.top = node.top.next
#         return node.top

#     def pop_at(self, stack):
#         pass

        # you hvae to reassing self.top how do I get that node?

class SetOfStacks():
    def __init__(self, value=None):
        self.node = Node(value)
        self.top = self.node

        self.capacity = 5
        self.stacks = [[self.top]]
        self.current_stack = 0

    def push(self, value):
        new_node = Node(value)
        current_stack = self.stacks[self.current_stack]
        if len(current_stack) >= self.capacity:
            self.stacks.append([new_node])
            self.current_stack += 1
            # this will not link the stacks together
        else:
            current_stack = self.stacks[self.current_stack]
            current_stack_node = current_stack[-1]
            current_stack_node.next = new_node
            new_node.next = self.top
            self.top = new_node
            current_stack.append(new_node)

    def pop(self):
        # remove the node from the list
        current_stack = self.stacks[self.current_stack]
        value = self.top.value
        if len(current_stack) == 1:
            self.stacks.pop()
            self.current_stack -= 1
            self.top = self.stacks[self.current_stack][-1]
        # im implementing this backwards the top should be the head of the list
        # if
        if len(current_stack) == 2:
            top = self.top
            # print(top, self.top)
            top.next = None
            self.stacks[self.current_stack].pop()
            self.top = current_stack[-1]
            self.top.next = None

        return value

        # unlink the node from the top

    def pop_at(self, stack_value):
        # we have access to the staks
        # ! we must re-assign the next of prev and next of current
        # of the nodes in the stacks if the index is greater than one and less than self.capacity
        stack = self.stacks[stack_value]
        _length = len(stack)
        # print(_length)
        value = stack[_length - 1].value
        if stack_value == self.current_stack:
            stack.pop()
            self.top.next = None
            self.top = stack[-1]

        else:
            stack[_length - 1].next = None
            stack.pop()  # the linked list doesn't go further than the array size so there is no resizing

        # if _length != self.current_stack:
        #     # the end of the array with the stack is the head
        #     # when i remove the head of a stack i just make the next none?
        #     stack.pop()

        return value

    def get_stacks(self):
        return self.stacks

    def get_stack_count(self):
        return self.current_stack

    def is_full(self, stack):
        if stack < len(self.stacks):
            return "Stack not in array"
        if len(self.stacks[stack]) == self.capacity:
            return "Stack is full"
        return "Stack is not full"

    def peek(self):
        return self.top.value


stack = SetOfStacks(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
# print(stack.top())
print("head", stack.peek())
print("Pop_at took:", stack.pop_at(0))  # takes 5 out
# print(stack.get_sta/cks())

print(stack.peek())  # shows 7
print(stack.pop())  # takes out 7
print(stack.get_stacks())
print(stack.peek())  # head shuold be 6
print(stack.pop())  # takes out 6

# print(stack.pop())
# print(stack.get_stacks())
print("Head after poping", stack.peek())

# print(stack.get_stacks())
# stacks = stack.get_stacks()
# for items in stacks:
#     for node in items:
#         print(node.value)
