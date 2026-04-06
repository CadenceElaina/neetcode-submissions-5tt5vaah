class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time = (target - position) / speed
        # we know a car will catch up to another if their time is <=  forming a car fleet
        res = 1
        stack = []
        # combine pos and speed into [[p, s]] using list comph
        pairs = [[p, s] for p, s in zip(position, speed)]
        for p, s in sorted(pairs, reverse=True):
            stack.append((target-p) / s) # decimal division not int division
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # do we have two items in our stack and is the top cars TIME slower than the cars TIME directly behind it?
                # if so we know they form a car fleet - pop - keep 1 car
                stack.pop()
        
        return len(stack)

