class Solution:
    def climbStairs(self, n: int) -> int:
        # n = 5
        memo = {}

        if n == 1 or n == 0:
            return 1

        if n in memo.keys():
            return memo[n]
        else:
            sub_result = self.climbStairs(n-1) + self.climbStairs(n-2)
            memo[n] = sub_result
            return memo[n]