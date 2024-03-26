from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = [k for k, v in Counter(nums).items() if v > len(nums)/2][0]
        print(result)
        return result