class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]


    def push(self, val: int) -> None:
        # <= handles duplicate mins!! 5->2->2
        # stack=[5,2,2,]
        # if you use val < self.lastMin then we get 
        # minStack =[5,2] instead of minStack = [5, 2, 2]
        # so if you pop once you would lose the duplicate and have min val = [5] instead of minStack = [5,2] after popping 2
        self.stack.append(val)

        # If minStack is empty, OR the new value is <= the current minimum
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        # If the value being popped is our current minimum, pop it from minStack too
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()



    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.minStack[-1]
