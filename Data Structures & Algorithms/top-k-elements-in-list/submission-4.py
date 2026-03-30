class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqOfNums = {}
        res = []
        #1 count freq of nums
        for num in nums:
            # if num in dict update value otherwise its 0 + 1
            freqOfNums[num] = freqOfNums.get(num, 0) +1
        # for 0 -> k add most freq values to our output array

        #2 create empty buckets where index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        #3 populate the buckets
        for num, freq in freqOfNums.items(): # loops through a tuple of an array with the key and values of the dict
        # ([k, v], [k1, v1], ... [kn, vn])
            buckets[freq].append(num) # in our buckets array at index of the frequency of the current key value pair
            # that we are looping through append the number (which is key) so that each index represents
            # the frequency of the numbers stored at that index in our buckets array
        
        #4 Get the top k elements
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res