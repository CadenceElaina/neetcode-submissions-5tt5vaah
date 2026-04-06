class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []

        for c in tokens:
            if c not in operators:
                stack.append(int(c))
            else:
                rightOp = stack.pop()
                leftOp = stack.pop()
                if c == "+":
                    res = leftOp + rightOp
                elif c == "-":
                    res = leftOp - rightOp
                elif c == "*":
                    res = leftOp * rightOp
                else:
                    res = int(leftOp / rightOp)
                stack.append(res)
        if stack:
            return stack.pop()
        else:
            return 0