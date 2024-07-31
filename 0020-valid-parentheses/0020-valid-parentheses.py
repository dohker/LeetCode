'''
- 스택
    - 첫 원소는 값 추가
    - 두 번째 원소 부터는 
        - open bracket이면 추가
        - close bracket이면 스택 마지막 값 확인 후 valid 체크
    - 스택에 남아 있는 원소가 없으면 True
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack