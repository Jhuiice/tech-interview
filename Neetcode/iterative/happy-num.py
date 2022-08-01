def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    n_cycle = [n]
    while True:
        n_str = str(n)
        n = 0
        for item in n_str:
            n += int(item)**2
        # break
        print(n)
        if n == 1:
            return True
        elif n not in n_cycle:
            n_cycle.append(n)
        else:
            break

    return False


print(isHappy(19))
print(isHappy(2))
