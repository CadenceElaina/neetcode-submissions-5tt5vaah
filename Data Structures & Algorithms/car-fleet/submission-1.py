class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
                    # time = (target - position) / speed  - for car to reach target
        # two cars will form a fleet if and only if the car ahead has a time greater than or equal to the time of the car behind it
        pairs = [[p, s] for p, s in zip(position, speed) ] # List comp.
        stack=[]

        for p, s in sorted(pairs)[::-1]: # reverse sorted order - start from front car back
            stack.append((target - p) / s) # decimal division
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop() # those two form a fleet - pop so that our stack tracks # of fleets
        
        return len(stack)