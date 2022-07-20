def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    # ! horrible wrong use the for loop list integration
    # x = ""
    # unwanted = "-:/\|[]{}!@#$%^&*()_~`+=,.\"' "
    # for char in s:
    #     if char not in unwanted:
    #         x += char
    # x = x.lower()
    # x_reverse = ""
    # # print(x)
    # # print(len(x))
    # for i in range(len(x)-1, -1, -1):
    #     # print(i)
    #     x_reverse += x[i]
    # print(x, x_reverse)
    # return x == x_reverse
    # palin = s.join([i for i in s if i.isalnum()]).lower()
    # return palin == palin[::-1]
    l, r = 0, len(s) - 1

    while l > r:
        while l > r and s[l].isalnum():
            l -= 1
        while l > r and s[r].isalnum():
            r += 1

        if s[l].islower() != s[r].islower():
            return False
        l, r = l-1, r+1

    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("a."))
print(isPalindrome("Marge, let's \"[went].\" I await {news} telegram."))
print(isPalindrome("race a car"))
print(isPalindrome("ab"))
