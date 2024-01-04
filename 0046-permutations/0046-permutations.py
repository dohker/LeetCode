class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        comb = []
        ans = []
        
        def backtrack():
            if len(comb) == len(nums):
                ans.append(comb[:])
                return
            
            for num in nums:
                if num not in comb:
                    comb.append(num)
                    backtrack()
                    comb.pop()
            
        backtrack()
        return ans
                