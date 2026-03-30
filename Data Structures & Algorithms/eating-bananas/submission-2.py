import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2 # find an estimation of k between lowest possible k and largest possible
            hours_spent  = 0
            for p in piles:
                #  1hr  ->    1hr ->   1hr = 3hrs              
                # 5 / 2 -> 3 / 2 -> 1 / 2 -> 0 = 3hrs
                hours_spent += math.ceil(p / k)
            
            if hours_spent <= h:
                res = k
                r = k -1 # jump to the middle of the LEFT half
            else:
                l = k + 1 # jump to middle of the RIGHT half
        return res

        