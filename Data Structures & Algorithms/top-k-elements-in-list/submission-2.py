class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCount = {}
        freqList = [[] for _ in range(len(nums) + 1)]
        res = []

        for num in nums:
            freqCount[num] = freqCount.get(num, 0) + 1
        for num, count in freqCount.items():
            freqList[count].append(num)
        for bucket in reversed(freqList):
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res