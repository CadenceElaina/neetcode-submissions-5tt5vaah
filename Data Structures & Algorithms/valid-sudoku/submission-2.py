import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # keep track of rows, cols, and 3x3s to see if we have duplicates
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                # if we have an empty cell just continue to avoid unneeded checks
                if val == ".":
                    continue
                
                # if this digit is already in this row (r) or col (c) or in the square return false
                # for squares r // 3 is 0 // 3 -> square 0
                # c // 3 - 0 // 3 -> square 0
                # r = 3 (4th index top row) // 3 = 1 square 1
                # c = 3 (4th index down in that row) square 5
                if val in rows[r] or val in cols[c] or val in squares[(r // 3, c // 3)]:
                    return False
                
                # add to our 3 dictionaries / hashmaps continaing our sets
                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3, c // 3)].add(val)
        return True 
                