class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(n, memo):
            if n == 1 or n == 0:
                return 1

            if n in memo.keys():
                return memo[n]

            else:
                sub_result = dp(n-1, memo) + dp(n-2, memo)
                memo[n] = sub_result
                return memo[n]

        return dp(n, memo)