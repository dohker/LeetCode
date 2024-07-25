class Solution:
    def rob(self, nums: List[int]) -> int:
        tabular = []

        tabular.append(nums[0]) # 0
        if len(nums) >= 2:
            tabular.append(max(nums[0], nums[1])) # 1

        for state in range(2, len(nums)):
            tabular.append(max(tabular[state-1], tabular[state-2] + nums[state]))
        return tabular[-1]