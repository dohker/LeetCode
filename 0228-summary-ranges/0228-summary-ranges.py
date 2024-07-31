'''
- 순회
- 비교
- 제한조건
    - 결과 배열의 마지막 원소가 '->'로 끝나면 '->' 제거
    - 결과 배열을 순회하면서 '->' 전후로 동일한 숫자라면 하나의 숫자로 변경
'''

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{nums[i - 1]}")
                start = nums[i]

        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[-1]}")

        return result