class Solution:
    def isValid(self, s: str) -> bool:
        
        mapping = {')': '(', '}': '{', ']': '['}

        stack = []
        for char in s:
            if char not in mapping:
                stack.append(char)
            else:
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False

        return False if stack else True