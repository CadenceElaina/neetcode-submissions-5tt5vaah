class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1 )]

        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


        # get frequencies
      #  for i in range(nums):
       #     val = nums[i]
      #      freq[nums] = freq.get(val,0)+1 # get value and update by one or create it at 0 and add 1

        # convert freq map to something you can loop over

        # loop backwards from end to k
