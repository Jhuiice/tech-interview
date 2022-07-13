# arrays and strings interview questions CTCI
# 1.1 is unique
# can also use a hash map to map out the letters in the string but this increase the space complexity
def isUnique(string):
    string = string.lower()
    for i in range(len(string)):
        for j in range(len(string) - 1, i, -1):
            if string[i] == string[j]:
                return False

    return True


# print(isUnique("Alex"), "1.1")
# print(isUnique("Alexa"), "1.1")


# ? 1.2

def isPermutation(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    string1Map = {}
    string2Map = {}

    for i in range(len(string1)):
        char = string1[i]
        if char not in string1Map:
            string1Map[char] = 1
        else:
            string1Map[char] += 1

    for i in range(len(string2)):
        char = string2[i]
        if char not in string2Map:
            string2Map[char] = 1
        else:
            string2Map[char] += 1

    if string1Map == string2Map:
        return (string1Map, string2Map)
    return (False, False)


# print(isPermutation("Alex", "xelA"), "1.2")
# print(isPermutation("Alex", "xelAa"), "1.2")

# this is the non scratch version
# ? 1.3 Urlify


def urlify(url):
    splitUrl = url.split()
    return "%20".join(splitUrl)


# print(urlify("John Snow"))
# print(urlify("John Snow from Burmingham"))


# ? 1.4 Palindrome Permutation
def palindromePermutation(word1, word2):
    if len(word1) != len(word2):
        return False

    perm1, perm2 = isPermutation(word1, word2)
    if not perm1:
        return False

    j = len(word1) - 1
    for i in range(len(word1)):
        if word1[i] != word1[j]:
            return False
        j -= 1
    return True


# print(palindromePermutation("racecar", "carrace"), "1.4 True")
# print(palindromePermutation("racecar", "racebar"), "1.4 False")
# print(palindromePermutation("radcecar", "racebar"), "1.4 False")
# print(palindromePermutation("racecar", "racebfddar"), "1.4 False")
# print(palindromePermutation("helleh", "lehhel"), "1.4 True")


# ? 1.5
# make three functions one for replace one for insert and one for remove
def replace(word, edit):
    count = 0
    for i in range(0, len(word)):
        if word[i] != edit[i]:
            count += 1

    if count <= 1:
        return True

    return False


def insert(s1, s2):
    count = 0
    index1 = 0
    index2 = 0
    while (index2 < len(s2) and index1 < len(s1)):
        if (s1[index1] != s2[index2]):
            if(index1 != index2):
                return False
            else:
                index1 += 1
                index2 += 1
            index2 += 1
        return True

# this is the whole problem in and of itself. Its a replacement of the three functions

#! this is currently incorrect


def oneEditAway(s1, s2):
    if len(s1) - len(s2) > 1:
        return False

    index1 = 0
    index2 = 0

    s1 = s1 if len(s1) < len(s2) else s2
    s2 = s2 if len(s1) < len(s2) else s1
    foundDifference = False
    while (index2 < len(s2) and index1 < len(s1)):
        if (s1[index1] != s2[index2]):
            if (foundDifference):
                return False
            foundDifference = True
            if (len(s1) == len(s2)):
                index1 += 1
        else:
            index1 += 1
        index2 += 1
    return True


def oneWay(word, edit):
    if len(word) - len(edit) > 1:
        return False

    if len(word) == len(edit):
        return replace(word, edit)

    if len(word) + 1 == len(edit):
        return insert(word, edit)

    if len(word) - 1 == len(edit):
        return insert(edit, word)


# print(oneWay("pale", "ple"))
# print(oneWay("pale", "pales"))
# print(oneWay("pale", "pleb"))
# print(oneEditAway("pale", "ple"))
# print(oneEditAway("pale", "pales"))
# print(oneEditAway("pale", "pleb"))

# string compression 1.6
# # there are many solutions to this algorithm

# this method is really slow and I also dont know how to implement the stringcompressor from page 89
def stringCompression(string):
    count = 0
    new_string = ""
    for i in range(1, len(string)):
        char = string[i]
        before = string[i - 1]
        count += 1
        if char != before:
            new_string += before
            new_string += str(count)
            count = 0

    return new_string


print(stringCompression("aabccccaaa"))
