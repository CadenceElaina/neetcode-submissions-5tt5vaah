class Solution:
    def isValid(self, s: str) -> bool:
        hm = {')' : '(', ']' : '[', '}' : '{' }
        stack =[]
        for c in s:
            if c in hm:
                if stack and stack[-1] == hm[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False