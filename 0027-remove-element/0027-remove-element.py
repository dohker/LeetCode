'''
nums int list
val int
val 제거
return len(nums)

nums는 Description의 Custom Judge에 의하면 Solution 클래스 외부의 전역 변수다.

nums 내에서 모든 val값을 제거해야 한다. nums 자체를 수정해야 한다. -> remove? pop?
제거된 값을 제외한 nums의 len을 return해야 한다.

ValueError가 발생하더라도 break하지 말고 continue를 해야 모든 nums의 요소들을 검사할 수 있다.
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        while True:
            if val not in nums:
                break
            try:
                nums.remove(val)
                k += 1
            except ValueError:
                continue
                
        return len(nums)