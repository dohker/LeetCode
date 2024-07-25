class Solution:
    def tribonacci(self, n: int) -> int:
        tabular = [0] * (n+1)

        if n == 0:
            return 0

        if n == 1 or n == 2:
            return 1

        tabular[0] = 0
        tabular[1] = 1
        tabular[2] = 1

        for i in range(3, n+1):
            tabular[i] = tabular[i-1] + tabular[i-2] + tabular[i-3]
        
        return tabular[n]