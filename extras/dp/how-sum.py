class Solution():
    def __init__(self, val):
        self.val = val

    #! Memo object gets stored in memory if it is declared as an argument
    # * My guess is the dictionary that is being passed is kept in memory for the entire
    # * Script for python
    def howSum(self, targetSum, numbers, memo):
        if targetSum in memo:
            return memo[targetSum]
        if targetSum == 0:
            return []
        if targetSum < 0:
            return None

        for num in numbers:
            remainder = targetSum - num
            value = self.howSum(remainder, numbers, memo)
            if value != None:
                memo[targetSum] = [*value, num]
                return [*value, num]

        memo[targetSum] = None
        return None


s = Solution(1)
s1 = Solution(2)
s2 = Solution(3)
s3 = Solution(4)
s4 = Solution(5)
s5 = Solution(6)


# ! When ran all numbers from each array are being used in later function calls
print(s.howSum(7, [2, 3], {}))
print(s1.howSum(7, [5, 3, 4, 7], {}))
print(s2.howSum(7, [2, 4], {}))
print(s3.howSum(8, [2, 3, 5], {}))
print(s4.howSum(300, [7, 14], {}))
