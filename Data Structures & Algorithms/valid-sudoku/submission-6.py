class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)


        for r in range(9):
            for c in range(9):
                pos = board[r][c]
                if pos == ".":
                    continue
                if pos in rows[r] or pos in cols[c] or pos in squares[(r//3, c//3)]:
                    return False
                rows[r].add(pos)
                cols[c].add(pos)
                squares[(r//3,c//3)].add(pos)
        return True
        # if any violation exit immedaite
        # skip "." squares
        #squares(rows // 3, cols //3)