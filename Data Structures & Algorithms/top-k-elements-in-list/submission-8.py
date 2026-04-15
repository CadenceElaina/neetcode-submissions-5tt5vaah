class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        # count freq
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        #place into buckets
        # have to add 1 to len of nums bc a num cant appear 0 times
        freq_buckets = [[] for _ in range(len(nums)+1)]

        for n, count in freq.items():
            freq_buckets[count].append(n)

        for i in range(len(freq_buckets) -1, 0, -1):
            for n in freq_buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res

        # looop backwards over buckets