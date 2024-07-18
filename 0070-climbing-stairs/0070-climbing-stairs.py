class Solution:
    def climbStairs(self, n: int) -> int:
        tabular = []
        tabular.append(1) # n = 0
        tabular.append(1) # n = 1
        
        for i in range(2, n+1):
            sub_result = tabular[i-1] + tabular[i-2]
            tabular.append(sub_result)
        
        return tabular[-1]