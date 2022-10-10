class Solution():
    def canSum(self, targetSum, numbers, memo={}):
        if targetSum in memo:
            return memo[targetSum]
        if targetSum == 0:
            return True
        if targetSum < 0:
            return False
        for num in numbers:
            remainder = targetSum - num
            if self.canSum(remainder, numbers, memo):
                memo[targetSum] = True
                return True

        memo[targetSum] = False
        return False


solution = Solution()
# * its caching my numbers list????
# print(solution.canSum(7, [2, 3]))  # True
# print(solution.canSum(7, [5, 3, 4, 7]))  # True
# print(solution.canSum(7, [2, 4]))  # False
# print(solution.canSum(8, [3, 9]))  # False
# print(solution.canSum(8, [2, 3, 5]))  # True
print(solution.canSum(300, [7, 14]))  # False

# print(canSum(13, [2, 9, 5, 12]))
# print(canSum(1, [9, 2]))
# print(canSum(7, [2, 4]))
# print(canSum(89, [2, 12]))
# print(canSum(300, [2, 12]))
