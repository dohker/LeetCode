class Solution:
    def majorityElement(self, nums: List[int]) -> int:

            count = 0
            candidate = None

            for num in nums:
                if count == 0:
                    candidate = num
                    print("candidate: {}, num: {}".format(candidate, num))
                count += (1 if num == candidate else -1)
                print(candidate, count)

            return candidate