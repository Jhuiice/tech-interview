# Given a string and a pattern, find out if the string contains any permutation of the pattern.

# Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

#     abc
#     acb
#     bac
#     bca
#     cab
#     cba

# If a string has ‘n’ distinct characters, it will have n!n!n! permutations.

# brute force and wrong

def find_permutation(str1, pattern):
    # TODO: Write your code here
    # must check pattern to the window of characters
    window_start = 0
    hash_map = {}
    permutation_counter = 0

    for window_end in range(len(str1)):
        # can only check the patter if the window is the same size
        right_char = str1[window_end]
        if right_char not in hash_map:
            hash_map[right_char] = 0
        hash_map[right_char] += 1

        # must comapare the size of the pattern to the length of window not hash_map
        # pattern must also be in the hash map is a while loop appropriate for this solution?

        while (window_end - window_start + 1) > len(pattern):
            # brute force method
            left_char = str1[window_start]
            for char in pattern:
                if char in hash_map:
                    permutation_counter += 1
                else:
                    permutation_counter = 0
            if permutation_counter == len(pattern):
                return False
            window_start += 1
            # how do I check it?

    return True

    # second attempt


def find_permutation(str1, pattern):
    # TODO: Write your code here
    # add all characters to a hash_map from the pattern. This will be the focused mapping
    pattern_char_hash = {}
    matches = 0
    window_start = 0

    for char in pattern:
        if char not in pattern_char_hash:
            pattern_char_hash[char] = 0
        pattern_char_hash[char] += 1

    # iterate over the str1 and compare the pattern hash
    for window_end in range(len(str1)):
        right_char = str1[window_end]

        if right_char in pattern_char_hash:
            pattern_char_hash[right_char] -= 1
            if pattern_char_hash[right_char] == 0:
                del pattern_char_hash[right_char]
            matches += 1

        if matches == len(pattern):
            return True

        if window_end - window_start + 1 > len(pattern):
            left_char = str1[window_start]
            if left_char not in pattern_char_hash:
                pattern_char_hash[left_char] = 0
            pattern_char_hash[left_char] += 1
            window_start += 1
            matches -= 1

        if len(pattern_char_hash) == 0:
            return True

    return False


# correct attempt

def find_permutation(str1, pattern):
    window_start, matched = 0, 0
    char_frequency = {}

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    # our goal is to match all the characters from the 'char_frequency' with the current window
    # try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency:
            # decrement the frequency of matched character
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            return True

        # shrink the window by one character
        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return False


def main():
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()


# same problem but add the starting indexes of anagram matches
def find_string_anagrams(str1, pattern):
    result_indexes = []
    # TODO: Write your code here
    # compare the pattern to the next n strings when you encounter the first char of the pattern in the string
    # if all strings match then the start index is added to the result index
    char_frequency = {}
    window_start = 0
    matched = 0
    # create a hash map

    for char in pattern:
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            matched += 1

        if matched == len(pattern):
            # must add window_start not window_end. Get the first index of the anagram not the last
            result_indexes.append(window_end)

        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return result_indexes


# actual answer from grokking

def find_string_anagrams(str1, pattern):
    window_start, matched = 0, 0
    char_frequency = {}

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    result_indices = []
    # Our goal is to match all the characters from the 'char_frequency' with the current window
    # try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency:
            # Decrement the frequency of matched character
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):  # Have we found an anagram?
            result_indices.append(window_start)

        # Shrink the sliding window
        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1  # Before putting the character back, decrement the matched count
                char_frequency[left_char] += 1  # Put the character back

    return result_indices


def main():
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))


main()
