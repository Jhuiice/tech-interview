# CTCI 4.7
# BUILD ORDER or more known as topological sort.
# this is a very hard and long problem that I do not understand as of July 16th, 2022

def build_order(tuple):
    left = tuple[0]
    right = tuple[1]  # right is dependent on the first
