class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        # get freq of each 
        for n in nums:
            count[n] = count.get(n,0)+1
        # loop over dict vals move freq to freq array where index = number off occurrences and each index stores an array of nums
        for n,c in count.items():
            freq[c].append(n)

        res=[]
        # loop backwards grabbing k elems
        for i in range(len(freq)-1,0,-1): # exclusive of zero bc no num can appear 0 times unless we wanted to store all nums outside the given nums array xddddddd
            for n in freq[i]: #loop over index to get all nums that occurred that index amount of times
                res.append(n)
                if len(res) == k:
                    return res
                