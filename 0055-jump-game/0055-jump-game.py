# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         # result = False
#         print("nums: {}".format(nums))
#         if nums[1]:
#             if nums[0] == 0:
#                 return False
#             return True
#         position = nums[1]
#         print("position==jump length: {}".format(position))
        
#         while True:
#             if nums[position] and position >= len(nums) or (position != len(nums) and nums[position] == 0):
#                 break
#             if nums[position]:
#                 self.canJump(nums[position+1:])
#                 # position += nums[position+1]
#             else:
#                 pass
            
#         return False





# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         max_reachable = 0  # 현재까지 도달할 수 있는 최대 인덱스
#         for i in range(len(nums)):
#             if i > max_reachable:
#                 return False  # 현재 위치에 도달할 수 없으면 False 반환
#             max_reachable = max(max_reachable, i + nums[i])  # 최대 도달 가능 거리 갱신
#             print("max_reachable: {}".format(max_reachable))
#             if max_reachable >= len(nums) - 1:
#                 return True  # 마지막 인덱스에 도달 가능하면 True 반환
#         return False





class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0  # 현재까지 도달할 수 있는 최대 인덱스
        for i, jump in enumerate(nums):
            if i > max_reachable:
                return False  # 현재 위치에 도달할 수 없으면 False 반환
            max_reachable = max(max_reachable, i + jump)  # 최대 도달 가능 거리 갱신
        return True