# describe how you could use a single array to implement three stacks
# * you could use a single array to implement three stacks by tracking 3 indexes
# * these three indexes are the start of the 3 stacks. The start of each stack will show
# * you the end of the last stack. Every time you insert or remove from the stacks you
# * must move all other data points in the array and update the start of each stack
# * if the index was behind the starting point
# * time complexity for removing and adding are O(N)
# * you could use three seperate arrays to keep track of the stacks, this would allow the creator to
# * keep track at static indexes but this would increase the space complexity to O(a + b + c) still O(N)

# * stacks starts, with a zero index, are 0, 1, 2
# * [None, None, None]
# * insert into stack 0 [1]
# * [[1], None, None], starting indexs are 0, 1, 2

# * insert into stack 1 [1,2,3,4]
# * [1, 1, 2, 3, 4, None], starting indexs are 0, 1, 5 now

# * with python we could use deque specifically if we were allowed to
