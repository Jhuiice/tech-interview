
# ! This is wrong and I dont know how to work around it yet. I could implement the stack with a list instead of a linked list
# it might be less data

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def set_min(self):
        # print(self.data)
        if self.next:
            # print(self.data)
            if self.next.data < self.data:
                self.min = self.next.data
            else:
                self.min = self.data
        else:
            self.min = self.data
        print("inside set_min", self.min)

    def get_min(self):
        print("inside get_min", self.min)
        return self.min


class MinStack(object):

    def __init__(self, data=None):
        self.head = Node(data)
        self.min = None
        self.size = 1 if data else 0
        # print("in minstack init", self.min)

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        head = self.head
        self.head = Node(val)
        # print(self.min)
        self.head.next = head
        self.min = self.head.get_min()
        if val < self.head.data:
            self.min = val
        print("inside push", self.min)

    def pop(self):
        """
        :rtype: None
        """
        head = self
        self = self.next
        return head

    def top(self):
        """
        :rtype: int
        """
        return self.head.data

    def getMin(self):
        """
        :rtype: int
        """
        # print(self.head.get_min())
        return self.head.get_min()


stack = MinStack(1)
# print(stack.top())
stack.push(2)
# print(stack.top())
stack.push(3)
# print(stack.top())


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
