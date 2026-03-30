class Solution:
    def trap(self, height: List[int]) -> int:
        # brute force check left most height against all others. calculate by looking at middle most square
        # between the two heights and checking its right and left if a square is above starting square that is
        # capable of holding water we would only then chec the squares to its right if so we keep checking right
        # and left until we hit a filled square. - then we continue until we reach the minimum of our two heights 
        
        if not height:
            return 0
        
        # initialize pointers at both ends
        l = 0
        r = len(height) - 1

        # track the highest bars seen so far from left and right
        left_max = height[l]
        right_max =height[r]

        res = 0

        # move pointers inward until they meet
        while l < r:
            # We strictly depend on the shorter of the two maximums
            if left_max < right_max:
                l += 1
                # update the max height seen from the left
                left_max = max(left_max, height[l])
                # add trapped water (if height[l] is the new max, this adds 0)
                res += left_max - height[l]
            else:
                r -= 1
                #update the max hieght seen from the right
                right_max = max(right_max, height[r])
                # add trapped water
                res += right_max - height[r]
        
        return res


            
        