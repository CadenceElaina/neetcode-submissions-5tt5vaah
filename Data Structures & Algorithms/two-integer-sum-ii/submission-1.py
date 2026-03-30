class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #non-decreasing order --- meaning either staying the same or increasing in values
        # index1 < index2 & idx1 + idx2 = target
        # target - val = difference
        # idx1 != idx2
        # cannot use same element twice
        # O(1) space & O(n) time
        # array is sorted
        # 1 pointer at start (smallest val since sorted) & 1 pointer at end (largest val)

        i = 0
        j = len(numbers)-1

        while(i < j):
            current_sum = numbers[i] + numbers[j] 

            if current_sum == target:
                return [i+1, j+1] #return 1-indexed not array indexed so add 1 from current idx
            elif current_sum > target:
                j -= 1
            else:
                i+=1
        
