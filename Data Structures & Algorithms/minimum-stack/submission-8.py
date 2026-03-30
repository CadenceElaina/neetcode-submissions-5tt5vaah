class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]


    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        # If minStack is empty, OR the new value is <= the current minimum


    def pop(self) -> None:
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()
        # If the value being popped is our current minimum, pop it from minStack too
        # If our minStack is empty we know we removed first value added to stack which was the first min val
        # so both are empty if minStack is empty



    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.minStack[-1]
