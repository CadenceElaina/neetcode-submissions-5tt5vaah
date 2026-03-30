class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # determine most frequent then 2nd most frequent to value of k
        # return an array/list of the values that are most frequent to value of k
        # hashmap keeping count of each unique number 
        # or maybe just a list where index 1 is most frequent followed by index 2 which is 2nd most freq etc for each value
        # ***index represents the frequency count!***
        # need to then look at highest freq within hashmap/dic up to k iterations adding those keys with highest freq to our final list/array
        # can sort the dictionary O(N log N) - sorted() function - make sure it sorts by values rather than its keys, use max heap approach O(N log k) - push all dic key-values to a heap - efficiently bubbles the most freq to the top
        #, or bucket sort O(N)!  - create brand new empty list of lists - make it the length of this list equal to the length of the original nums array + 1
        # Why? because the maximum frequency any number can possibly have is the length of the array (i.e., if every number in the array is 1).
        # the index of this new list becomes the freq.
        # teh value at that index is a list of numbers that showed up that many times.
        # once populated loop backwards from highest to zero grabbing until we reach k items.
        # takes a little more memory 

        freqOfNums = {}
        # Step 1: Count the frequencies
        for num in nums:
            freqOfNums[num] = freqOfNums.get(num, 0) + 1
        
        # Step 2: Create empty buckets where index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        # Step 3: Populate the buckets
        for num, freq in freqOfNums.items():
            buckets[freq].append(num)
        
        #Step 4: Gather the top k elements by reading buckets backwards
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result)==k:
                    return result
