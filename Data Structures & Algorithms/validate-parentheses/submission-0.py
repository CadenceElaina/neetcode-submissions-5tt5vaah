class Solution:
    def isValid(self, s: str) -> bool:
        #big O(n) - time and space
        # use a stack
        # use a hashmap for checking the correct value expected if not return false
        # else add character to stack
        # exiting the loop over the string we check to make sure the stack is empty returning true if empty or false if not
        stack = []
        hashmap = {')': '(', ']' : '[', '}' : '{'}

        for c in s:
            if c in hashmap:
                if stack and stack[-1] == hashmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else: 
            return False
