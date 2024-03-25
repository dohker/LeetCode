'''
nums1 array asc, m int
nums2 array asc, n int
merge nums1, nums2 -> nums1 which is asc(sorting)

nums1에서 find/index를 이용하여 0의 위치를 찾는다.: O(n)
-> find는 값을 찾지 못한 경우 -1을 반환할 수 있는데 제약조건에서 음수값도 들어갈 수 있으므로 index를 쓴다.
해당 위치부터 nums2 요소들을 채운다.: O(n)
nums1을 sorted한다. -> O(nlogn)이 걸릴 것
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        try:
            first_zero_index = nums1.index(0)
            nums1[m:m+n+1] = nums2[:]
            nums1.sort() # nums1 = sorted(nums1): 에러
        except:
            pass