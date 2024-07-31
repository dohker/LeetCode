'''
- 순회
- 비교
- 제한조건
    - 결과 배열의 마지막 원소가 '->'로 끝나면 '->' 제거
    - 결과 배열을 순회하면서 '->' 전후로 동일한 숫자라면 하나의 숫자로 변경
'''

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        prev = nums[0]
        output = [str(prev)+"->"]

        for i in range(1,len(nums)):
            if (nums[i]-prev) != 1:
                output[-1] = output[-1]+str(prev)
                output.append(str(nums[i])+"->")
            if i == len(nums)-1 and (nums[i]-prev) == 1:
                output[-1] = output[-1]+str(nums[i])
            prev = nums[i]
        
        if output[-1].endswith('->'):
            output[-1] = output[-1].replace('->', '')
        for idx, value in enumerate(output):
            temp = value.split('->')
            if len(temp) >= 2 and temp[0] == temp[1]:
                output[idx] = temp[0]

        return output