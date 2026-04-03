class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        res = [] 

        for num in nums:
            freq[num] = freq.get(num, 0 )+1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, f in freq.items():
            buckets[f].append(num)
        
        for i in range(len(buckets) -1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        