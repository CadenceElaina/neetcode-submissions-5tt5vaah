class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #brute force
        res = 0

        for l in range(len(heights)):
            for r in range(l + 1, len(heights)):
                area = (r - l) * min(heights[l], heights[r]) # w*l (width = right pointer - left pointer, height = our minimum height of the value at our left pointer and our right pointer)
                res = max(res, area) # everytime we find a larger area we update our area
        return res