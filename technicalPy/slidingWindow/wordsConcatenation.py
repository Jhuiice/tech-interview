# words concatentation (hard)

# first attempt
#! I broke the words down to characters. You can accomplish this without it.
#! remember to look for edge cases!
def find_word_concatenation(str1, words):
    result_indices = []
    # TODO: Write your code here
    # need starting indices
    window_start = 0
    char_frequency = {}
    matched = 0
    concat_length = len("".join(words))
    # how is this similiar to sliding glass window? The words must be used foward and backward
    # how can I do that?
    # map the words to a hash table
    for word in words:
        for char in word:
            if char not in char_frequency:
                char_frequency[char] = 0
            char_frequency[char] += 1

    for window_end in range(len(str1)):
        right_char = str1[window_end]

        if right_char in char_frequency:
            char_frequency[right_char] += 1
            # greator or equal to zero for duplicates # this feels wrong
            if char_frequency[right_char] >= 0:
                matched += 1

        if matched == concat_length:
            result_indices.append(window_start)

        while window_end - window_start + 1 > concat_length:  # this is also wrong
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                char_frequency[left_char] += 1
                if char_frequency[left_char] >= 1:  # i feel like this is wrong too
                    matched -= 1

    return result_indices


# grokking answer
def find_word_concatenation(str1, words):
    if len(words) == 0 or len(words[0]) == 0:
        return []

    word_frequency = {}

    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 0
        word_frequency[word] += 1

    result_indices = []
    words_count = len(words)
    word_length = len(words[0])

    for i in range((len(str1) - words_count * word_length)+1):
        words_seen = {}
        for j in range(0, words_count):
            next_word_index = i + j * word_length
            # Get the next word from the string
            word = str1[next_word_index: next_word_index + word_length]
            if word not in word_frequency:  # Break if we don't need this word
                break

            # Add the word to the 'words_seen' map
            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1

            # No need to process further if the word has higher frequency than required
            if words_seen[word] > word_frequency.get(word, 0):
                break

            if j + 1 == words_count:  # Store index if we have found all the words
                result_indices.append(i)

    return result_indices


def main():
    print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
    print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))


main()
