class Solution:
    def trap(self, height: List[int]) -> int:

        # if we reach a higher height then we need to determine space between that can hold water
        # water can only rise to the height of min outer barrier (right or left) 
        # so any heights smaller than the outer bounds can hold water 
        # min(left bound, right bound) - height for each height between bounds 
        # track sum and return total
        # careful about spots that dont have a right or left bound.

        l = 0
        r = len(height)-1
        left_max =  height[l]
        right_max = height[r]
        res = 0
        while l < r:
            if left_max < right_max:
                l+=1
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            else:
                r-=1
                right_max = max(right_max, height[r])
                res+= right_max - height[r]
        return res
 
