# Longest subtstring with maximim K distinct characters
# sliding window is using a range of indexes instead of iterating over the entire list every time
# this improves the Big O notation runtime
# it uses arrays, for loops, while loops, and hash maps
# time complexity is O(N) we iterate over the entire string of length N
# space complexity is O(K) we will only store O(k+1) characters

def solver(k, str1):
    # this is noise
    if (str1 == ""):
        return 0

    window_start = 0
    letter_map = {}
    max_length = 0

    for window_end in range(len(str1)):
        char = str1[window_end]
        if char not in letter_map:
            letter_map[char] = 0
        letter_map[char] += 1
        while len(letter_map) > k:
            begin_char = str1[window_start]
            letter_map[begin_char] -= 1
            if letter_map[begin_char] == 0:
                del letter_map[begin_char]
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length


print(solver(2, 'araaci'))
print(solver(1, 'araaci'))
print(solver(3, 'cbbebi'))
print(solver(10, 'cbbebi'))
