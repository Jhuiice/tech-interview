# *
# ? how would you implement a min function to a stack and make it O(1) run time?
# ? push and pop will be a O(1) run time also

# * since push and pop are O(1) there is no sorting being done behind the scenes
# * in your stack object you would have a self.min value and everytime a value
# * is pushed to the stack it would check it and compare the values if removed
# * how would it handle that? min would need to hold 2 values?
# * each node would hold a self.min value of the value that is the smallest beneath it
# * the top node would have the data of all the other minimums
# * how would I calculate this when we pop and push nodes?
# * everytime a node is added to the stack it checks the min value below it
# * then it comapares it to itself and whatever value is smaller the new self.min value is changed
# * when the top node is popped, if it is the minimum of the stack the new self min will not change below it
# * if the top node is popped and is not the minimum value then all is well
