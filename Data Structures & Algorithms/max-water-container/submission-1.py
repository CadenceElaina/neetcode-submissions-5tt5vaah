class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
#            elif heights[l] > heights[r]:
       #        r -=1
        l = 0
        r = len(heights)-1
        while l  < r:
            area = (r-l) * min(heights[l], heights[r])
            res = max(res, area)
            if heights[l] < heights[r]:
                l +=1
            else:
                r -= 1

        return res