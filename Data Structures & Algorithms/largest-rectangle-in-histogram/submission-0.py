class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # loop through bars
        # if next bar is taller or same height as starting point of this area continue
        # once you reach a shorter bar from the initial stop - calculate area - update max if necessary max(maxArea, curArea)
        # store indices on a stack
        #  monotonic increasing
        # when we see a shorter bar - pop the top index off the stack - this is the height of the rectangle we are about to calculate
        # width = right boundary ;
        # Area = Height * (Right - Left - 1)
        
        maxArea = 0
        stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
                start = i
                while stack and stack[-1][1] > h: # if we have items in stack and the top item's height is > curr h
                # then we have to pop that item as it cant extend to our curr h
                # calc max height
                    index, height = stack.pop()
                    maxArea = max(maxArea, height * (i - index))
                    start = index
                stack.append((start, h))
                
        # any reamining rect in stack at end extended until last index
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea