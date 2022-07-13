
# implement a que with two stacks
# how the hell do I do that?
# i can have two stacks equal the same thing but one stack will be the reverse of the other?
# when you pop onto another list that will reverse the order of the stacks

from distutils.dep_util import newer


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
        item = self.top  # .value
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
        return self.top == None  # or self.node.value == None

    def reverse(self):
        head = self.top
        prev = None
        while head is not None:
            next = head.next  # pointer to the next node ( a holder object )
            head.next = prev  # the next pointer of head goes to prev
            prev = head  # prev is now equal to the head
            head = next  # the head is now transfered to the next node

        return prev


def reverse_stack():
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next

    return prev

# TODO finish this when your brain doesn't feel fried


class MyQueue():
    def __init__(self):
        self.newest_vals = Stack()  # start of the queue
        self.oldest_vals = Stack()  # end of the queue
        self.size = 0

    def add(self, value):
        # push to the head
        self.newest_vals.push(value)  # pushes to head
        # self.oldest_vals.push(value)  # pushes to tail

    def remove(self):
        # reverse the stack give it to a value and remove the head
        # value1 = self.newest_vals.pop(value)
        # value2 = self.oldest_vals.pop(value)
        self.shift_stacks()
        # return self.oldest_vals.pop()
        return self.newest_vals.pop()
        # return self.oldest_vals.pop()
        # when you pop for a queue you need the tail end of the stack
        # return(value1, value2)

    def shift_stacks(self):
        # print(self.oldest_vals.peek())
        # print(self.oldest_vals.is_empty())
        # print(self.oldest_vals)
        print(self.newest_vals.is_empty())
        if (self.oldest_vals.is_empty()):
            while (not self.newest_vals.is_empty()):
                self.oldest_vals.push(self.newest_vals.pop())
                print(self.oldest_vals.value)

    def peek(self):
        return (self.newest_vals.peek(), self.oldest_vals.peek())


queue = MyQueue()
queue.add(2)
print(queue.peek())
queue.add(3)
print(queue.peek())
print("remove", queue.remove().value)

print(queue.peek())
