class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return nested list if more than one correct result
        # no matches return empty array
        # nums[i] + nums[j] + nums[k] == 0 
        # i mean loop through array and check if the current value  with two others = 0
        # so on that value we run a two pointer approach with left and right indexes
        # to check all numbers except our current to see if the current smallest value / pointer + our largest pointer from the other side + our current number in outter loop == 0 if so add it to list as a list. 
        
        result = []
        
        # 1. Sort the array first so the two-pointer math works
        nums.sort()
        
        # 2. Outer loop: Use an index 'i' so we can position our left pointer
        for i in range(len(nums)):
            # If our current number is > 0, we can stop. 
            # Since the array is sorted, no positive numbers added together will ever equal 0.
            if nums[i] > 0:
                break
            
            # Skip duplicates for the outer loop to prevent duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 3. Inner loop: Set up the two pointers
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # 4. Pointer movement logic
                if current_sum < 0:
                    left += 1  # We need a bigger number
                elif current_sum > 0:
                    right -= 1 # We need a smaller number
                else:
                    # We found a match!
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Move both pointers inward to look for the next potential combination
                    left += 1
                    right -= 1
                    
                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
        return result

  
                    # [-2, -2, 0, 0, 2, 2]

       
        
