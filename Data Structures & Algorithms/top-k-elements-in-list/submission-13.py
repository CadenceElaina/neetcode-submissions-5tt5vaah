class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for i in range(len(nums)+1)]
        #store freq at loc in freq[] where index rep. occ.
        for n in nums:
            count[n] = count.get(n,0)+1
        
        for n,c in count.items():
            freq[c].append(n)
        
        res=[]
        # loop backwards over bucket array getting k items
        for i in range(len(freq)-1, 0, -1): #stop at before 0 since index 0 rep. 0 occurences 
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            