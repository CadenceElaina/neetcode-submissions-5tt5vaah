import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
                for c in range(9):
                    val = board[r][c]

                    # if empty cell continue 
                    if val == ".":
                        continue

                    # 3 checks return false if met
                    if val in rows[r] or val in cols[c] or val in squares[(r // 3, c // 3)]:
                        return False

                    # add to our 3 dictionaries containing the sets
                    rows[r].add(val)
                    cols[c].add(val)
                    squares[(r // 3, c // 3)].add(val)
        return True 