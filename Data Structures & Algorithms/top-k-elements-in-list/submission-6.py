class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} # feq map
        res = []
        # tuple as key but not a list
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        # buckets - list of lists where the index reps the freq - buckets[3] holds numbers taht appear 3 times
        freq_buckets = [[] for _ in range(len(nums) + 1)]

        # fill buckets 
        for n, count in freq.items():
            freq_buckets[count].append(n)

        # loop backewards over buckets until we get k elements
        # for each index in our buckets lopo through its list at each index
        for i in range(len(freq_buckets)-1, 0, -1):
            for n in freq_buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res           