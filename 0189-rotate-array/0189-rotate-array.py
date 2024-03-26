class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        while cnt < k:
            nums.insert(0, nums[-1])
            nums.pop(-1)
            cnt += 1