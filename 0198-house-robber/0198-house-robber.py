'''
state: 현재 집의 위치

상태 전이:
    f(3) = max(1 + f(2) or 1 + f(2))
    f(2) = 3 + f(1) or 3 + f(0)
    f(1) = 2
    f(0) = 1

base case:
    f(1) = 2
    f(0) = 1

dp(state) = max(nums[state] + dp(state-1), nums[state] + dp(state-2))

if state in memo.keys():
    return memo[state]
else:
    memo[state] = max(nums[state] + dp(state-1), nums[state] + dp(state-2))
    return memo[state]
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(state: int):
            if state == 0:
                return nums[0]
            if state == 1:
                return max(nums[0], nums[1])

            if state not in memo.keys():
                memo[state] = max(dp(state-1), dp(state-2)+nums[state])

            return memo[state]

        memo = {}
        return dp(len(nums)-1)