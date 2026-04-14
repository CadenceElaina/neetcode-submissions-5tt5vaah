class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #
        freq = {}
        res = []

        for n in nums:
            freq[n] = 1 + freq.get(n,0)

        # buckets - list of lists where the index reps the freq  - buckets[3] holds numbers that appear 3 times

        freq_buckets = [[] for _ in range(len(nums)+1)]

        # fill buckets
        for n, count in freq.items():
            freq_buckets[count].append(n)

        # lop backwards over bucket until we get k elements
        for i in range(len(freq_buckets)-1, 0, -1):
            for n in freq_buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res
        # use list to store numbers

        # make list into key to store in dict