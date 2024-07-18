class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def backtrack(start, memo):
            if start == len(s):
                return True
            if memo[start] is not None:
                return memo[start]
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordDictSet and backtrack(end, memo):
                    memo[start] = True
                    return True
            memo[start] = False
            return False
        
        wordDictSet = set(wordDict)
        memo = [None] * len(s)
        return backtrack(0, memo)