# CTCI # 8.6 Towers of Hanoi

# implement problem using 3 stacks

from collections import deque


def toh(n):
    # head is on the left
    stack1 = deque([])
    stack2 = deque([])
    stack3 = deque([])

    # initialize first tower
    for i in range(n):
        stack1.append(i)

    # What are we keeping track of ?
    # We need to keep track of moves ?
    # What are the common subproblems ?
    # What are our subproblems ?
    # * sub problem would be to move the disks onto the other stacks.
    # * if a disk can't fit on either stick change stack and move the disk to the 3rd first
    # * if not the third than the first.
    # * if no move revert back to prior move?
    # the stack needs to optimize approaches and keep track of them
    # this will be needed for backtracking prior moves to revert to
    # and checking moves that do not work
    # ? is there a randomness to this or will the program execute the same the entire time?
    # ! higher numbers cannot be above, in this case, to the left of a smaller number, in our stack
    # ? designated starting stack? We could choose starting stack but that would change the result of our time complexity
    # ! this is of stack of n
