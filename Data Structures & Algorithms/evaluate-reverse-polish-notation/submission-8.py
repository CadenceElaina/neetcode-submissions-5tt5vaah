class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # so RPN works by pushing values onto our stack
        # once we reach an operator (+, -, /, *) we pop last two numbers off stack perform calculation and push it onto stack
        # we continue process until we reach the end? / empty stack and return final result
        operation = ["+", "-", "*", "/"]
        stack = []

        for c in tokens:
            if c not in operation:
                stack.append(int(c))
            else:
                rightOp = stack.pop()
                leftOp = stack.pop()
                if c =="*":
                    res = leftOp * rightOp
                elif c=="/":
                    res = int(leftOp / rightOp) # python uses dec division by default
                    # // -> rounds down to -infinity where as java and others do 6/4 -> 1
                    # -6/4 int(-1.5) -> -1 vs -6//4 -> -2
                elif c=="+":
                    res = leftOp + rightOp
                else:
                    res = res = leftOp - rightOp
                stack.append(res)
        if stack:
            return stack.pop()
        else:
            return 0