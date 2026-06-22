class Solution:
    def isValid(self, s: str) -> bool:
        brack_stack = []
        mapping = {']': '[', ')': '(', '}': '{'}

        for char in s:
            if char in mapping:
                if brack_stack and brack_stack[-1] == mapping[char]:
                    brack_stack.pop()
                else:
                    return False
            else:
                brack_stack.append(char)
        return not brack_stack
