'''
ransomNote의 원소를 일일이 hash 테이블에 넣는다. 키는 문자열, 밸류는 카운트
전체 개수를 카운팅하는 변수를 둔다.
magazine을 순회하면서 한 글자씩 hash 테이블에서 찾아서 밸류를 뺀다. 
만약 magazine에 있는 게 ransomNote에 없다면 continue
전체 개수를 카운팅하는 변수에서 값을 뺀다.
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_table = {}
        result = 0
        for i in ransomNote:
            if i not in hash_table:
                hash_table[i] = 0
            hash_table[i] += 1
            result += 1
        

        for j in magazine:
            if j in hash_table and hash_table[j] != 0:
                hash_table[j] -= 1
                result -= 1
            if result == 0:
                return True
        
        if result == 0:
            return True
        return False