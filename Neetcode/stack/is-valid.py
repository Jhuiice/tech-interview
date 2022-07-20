def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    # counter parts dict?
    counter_part = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

    i = 1
    while i < len(s):
        if s[i-1] not in counter_part:
            return False
        if counter_part[s[i-1]] != s[i]:
            return False
        i += 2
    return True


print(isValid("()"))
print(isValid("(("))
print(isValid("()()"))
print(isValid("{}(]"))
