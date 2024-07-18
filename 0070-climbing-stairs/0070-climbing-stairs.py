class Solution:
    def climbStairs(self, n: int) -> int:
        tabular = [1, 1] # n = 0, 1
        
        for i in range(2, n+1):
            tabular.append(tabular[i-1] + tabular[i-2])
        
        return tabular[-1]