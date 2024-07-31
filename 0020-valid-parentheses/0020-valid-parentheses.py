'''
- 스택
    - 첫 원소는 값 추가
    - 두 번째 원소 부터는 
        - open bracket이면 추가
        - close bracket이면 peek으로 스택 값 확인 후 valid 체크
    - 스택에 남아 있는 원소가 없으면 True
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = [s[0]]

        for i in range(1, len(s)):
            if s[i] in (')', ']', '}'):
                if len(stack) == 0:
                    return False
                match stack[-1]:
                    case '(':
                        if s[i] == ')':
                            stack.pop()
                        else:
                            stack.append(s[i])
                    case '[':
                        if s[i] == ']':
                            stack.pop()
                        else:
                            stack.append(s[i])
                    case '{':
                        if s[i] == '}':
                            stack.pop()
                        else:
                            stack.append(s[i])
                    case _:
                        stack.append(s[i])
            else:
                stack.append(s[i])
        print(f'stack:{stack}')
        if len(stack) == 0:
            return True
        return False
        