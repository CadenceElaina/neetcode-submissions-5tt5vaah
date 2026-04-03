
        # look at middle of rows -> is this correct row compare first and last to target ->
        # move pointer up or down a row until were on the right row -> once on correct row we 
        # perform binary search 
        # compare first integer of row and last integer of row to target and adjust pointers


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        # STEP 1: Binary search to find the correct row
        top, bot = 0, rows - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]: 
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:  
                # Target is within the range of this row
                break
        
        # If the loop finished without finding a valid row range
        if not (top <= bot):
            return False
        
        # STEP 2: Binary search within the identified row
        # (row is already set from the 'break' in Step 1)
        row = (top + bot) // 2
        l, r = 0, cols - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]: # Fixed: changed > to <
                r = mid - 1
            else:
                return True
            
        return False
