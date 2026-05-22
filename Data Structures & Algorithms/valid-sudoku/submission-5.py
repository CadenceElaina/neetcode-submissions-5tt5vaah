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
                if pos in rows[r] or pos in cols[c] or pos in squares[(r // 3, c //3)]:
                    return False
                
                cols[c].add(pos)
                rows[r].add(pos)
                squares[(r//3, c//3)].add(pos)
        return True