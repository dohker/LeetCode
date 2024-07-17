from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True  # 빈 문자열은 항상 wordDict의 단어들로 구성될 수 있다.

        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i >= len(word) and dp[i - len(word)] and s[i - len(word):i] == word:
                    dp[i] = True
                    break

        return dp[len(s)]
