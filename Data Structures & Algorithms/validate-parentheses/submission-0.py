class Solution:
    def isValid(self, s: str) -> bool:
        brack_stack = []
        mapping = {']': '[', ')': '(', '}': '{'}

        for char in s:
            if char in mapping:
                top_stack = brack_stack.pop() if brack_stack else '#'
                if mapping[char] != top_stack:
                    return False
            else:
                brack_stack.append(char)
        return not brack_stack
