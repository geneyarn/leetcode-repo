class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                last = stack[-1] if stack else ''
                if c == ')' and last != '(':
                    return False
                elif c == '}' and last != '{':
                    return False
                elif c == ']' and last != '[':
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
