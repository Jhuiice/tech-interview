# CTCI 8.4 Power set

def power_set(sett):
    # find all subsets of a set
    # ? What does this mean? What are we targeting?
    # find a certain distinc subsets? and hash them?
    # this is a set set(a,b,c,d) = {a,b,c,d}
    # how would you make combinations of this?
    # {a},{b},{c} are subsets of {a,b,c}
    # We can hash a subset
    # we cant iterate over a set
    # sets are distinct can we calculate the number or subsets based on the len? This wouldn't prove useful
    #! recurse or use bottom up approach?
    # Bottom up and iteratation (tabulation)
    # top down and recursion creating the lead of the subproblems?

    # to check subsets {a,b,c} the combination of any of them will be in the subset
    # to find this we need to use a left and right aproach either using recursion or iteration with a for => while loop

    # for i in range(n) # can't subsript a set. We can enumerate over it
    # * enumerate pulls an index and the value of the index
    # * ex
    # * sub = {'a', 'b', 'c'}
    # * for index, value in enumerate(sub):
    # *     print(index, value)
    # *
    # * output
    # * => 0, 'a'
    # * => 1, 'b'
    # * => 2, 'c'

    # ? How would i use this to my advantage?

    subsets = []
    # for item in sett:
    #     subsets.append({item})
    # return subsets
    current_index = 0
    # ? all subsets are combinations?
    for index, value in enumerate(sett):
        subsets.append({value})  # have index 0, 1, 2 as {'a', 'b', 'c'} ?
        i = index
        while i > 0:
            # ? how do we append and create subsets?
            # ? we use the subsets array to iterate over prior cases
            subsets[current_index] = subsets[i]


print(power_set({"a", "b", "c"}))

# NOTE can use bit manipulation here because the letter is either in or out a yes/no a 1/0
