class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time = (target - pos) / speed
        stack =[]
        pairs = []

        for i, p in enumerate(position): 
                pairs.append([p, speed[i]])

        pairs.sort()        
        pairs.reverse()
        for pair in pairs:
            time = (target - pair[0]) / pair[1]
            stack.append(time)
            if stack and len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
