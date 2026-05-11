class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums) - 1
        m = length // 2
        l = 0
        h = length
        # searching a massive array where both l and r are very large 
        # l = 1,500,000,000 and r = 2,000,000,000, sum = 3,500,000,000 - 3.5b > 2.147b (int limit for most languages - value "wraps around" in memory - typically resulting in a negative number)
        # l + ((r-l) // 2) == (l+r)//2 but it calculates midpoint differently
        # m = l +  r-l/2 = 2l+r-l / 2 = l+r / 2
        # 8+10 = 18 / 2 = 9
        # 10-8=2 inches , 2/2 = 1 inch + 8 = 9in
        while l<= h:
            m = l+((h-l)//2)
            if nums[m] == target:
                return m
            if nums[m] > target:
                h = m-1
            else:
                l = m+1
        return -1