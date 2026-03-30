class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]
        self.topVal = 0
        self.lastMin = sys.maxsize


    def push(self, val: int) -> None:
        if val <= self.lastMin:
            self.minStack.append(val)
            self.lastMin = val
        self.stack.append(val)
        self.topVal = val

    def pop(self) -> None:
        if self.top() == self.lastMin:
            # check if minStack is not empty and if so update lastMi
            self.minStack.pop()
        if len(self.minStack) == 0:
            self.lastMin = sys.maxsize
        else:
            self.lastMin = self.minStack[-1]
        self.stack.pop()
        self.topVal = self.stack[-1] if self.stack else 0


    def top(self) -> int:
        return self.topVal


    def getMin(self) -> int:
        return self.lastMin
