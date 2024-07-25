class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [-1] * n

        def dp(i: int) -> int:
            if i < 0:
                return 0
            if memo[i] != -1:
                return memo[i]
            if i == 0 or i == 1:
                memo[i] = cost[i]
            else:
                memo[i] = cost[i] + min(dp(i - 1), dp(i - 2))
            return memo[i]

        return min(dp(n - 1), dp(n - 2))