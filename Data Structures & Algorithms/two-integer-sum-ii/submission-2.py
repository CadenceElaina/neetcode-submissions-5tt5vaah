class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while (i < j):
            # if i + j = target return indexes
            # else check if we need a higher sum - move i forward or lower sum - move j backwards
            current_sum = numbers[i] + numbers[j]
            if current_sum == target:
                return [i+1, j+1] # want 1-indexed value / pos not using standard array indexing
            elif current_sum > target:
                j -= 1
            else:
                i += 1