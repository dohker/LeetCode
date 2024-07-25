class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(state: int):
            if state == 0:
                return nums[state]
            if state == 1:
                return max(nums[state-1], nums[state])

            if state not in memo.keys():
                memo[state] = max(dp(state-1), dp(state-2)+nums[state])
            
            return memo[state]
        return dp(len(nums)-1)