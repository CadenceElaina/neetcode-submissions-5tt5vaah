class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time = (target - position) / speed  - for car to reach target
        # two cars will form a fleet if and only if the car ahead has a time greater than or equal to the time of the car behind it

        pair = [[p, s] for p, s in zip(position, speed)] #list comp
        
        stack = []
        for p, s in sorted(pair)[::-1]: #reverse sorted order
            stack.append((target - p) / s) #python is decimal division - time
            # need 2 cars to form car fleet & time to destination 
            #at top of stack is less than the next item in the stack - they collide
            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                stack.pop()
        return len(stack)