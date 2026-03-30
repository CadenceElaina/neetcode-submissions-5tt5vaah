class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # non-dec - 0, 0, 1, 1, 1, 2, 3, 5, 5, 9, ... 
        # 1     2 4 8
        # 10    11 12 13
        # 14    20 30 40
        # O(log(m * n))
        #cols = len(matrix[0]) - 1
       # row = len(matrix) - 1
        # just look at matrix[0][middle of length of rows] - is our val > target or < target
        # look at end val of that row and check if its > or < target... - if its greater than and our initial
        # start of row is less than we know its in that row
        # otherwise we need to move up or down
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS - 1

        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        if not (top <= bottom):
            return False
        
        l, r = 0, COLS -1
        row = (top + bottom) // 2
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False



