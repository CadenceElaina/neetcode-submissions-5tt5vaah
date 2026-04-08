import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min hours = len of piles 
        # if our h = len(piles) then our min speed has to be the max val in piles
        # range abs min is 1 and max speed is our len of piles
        # 1 <= speed <= size_of_largest_pile

        l = 1 # our min speed
        r = max(piles)
        best_speed = r

        while l <= r:
            m = (l + r) // 2

            total_hours = 0
            for p in piles:
                total_hours += math.ceil(p / m)
            
            if total_hours <= h:
                best_speed = m
                r = m - 1
            else:
                l = m + 1
        return best_speed 
