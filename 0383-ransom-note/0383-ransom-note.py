class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_table = {}

        # ransomNote의 각 문자를 해시 테이블에 추가
        for char in ransomNote:
            if char not in hash_table:
                hash_table[char] = 0
            hash_table[char] += 1

        # magazine의 각 문자를 해시 테이블에서 제거
        for char in magazine:
            if char in hash_table:
                hash_table[char] -= 1
                if hash_table[char] == 0:
                    del hash_table[char]
                if not hash_table:
                    return True

        return not hash_table