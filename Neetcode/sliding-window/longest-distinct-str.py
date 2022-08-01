def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    # if len(s) == 1:
    #     return 1
    l, r = 0, 0
    # how can i keep track of l:r
    maxi = 0
    while l <= r and r <= len(s) - 1:
        # print(s[r], s[l:r])
        if s[r] in s[l:r]:
            # print("r in set")
            l += 1
        else:
            r += 1
        maxi = max(maxi, r-l)
    # print(r)
    return maxi


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbb"))
print(lengthOfLongestSubstring("au"))
print(lengthOfLongestSubstring("b"))
print(lengthOfLongestSubstring("bvbf"))

# ! This is not working with edge cases where the range lands on the last index
# ! this is wrong because I am resetting the l to r if there are any duplicates in the subarray regardless of where the duplicates are
