import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # initialize collections to track seen values
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                #skip empty cells
                if val == ".":
                    continue
                
                # check for duplicates against constraints (rows, cols, squares)
                if (val in rows[r] or
                        val in cols[c] or
                        val in squares[(r // 3, c // 3)]):
                        return False
                
                # add to sets for future checks
                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3, c // 3)].add(val)
        return True
        # 1-9 no duplicates in a row
        # each col must have 1-9 no duplicates
        # each of the nine 3x3 sub-boxes must contain 1-9 no duplciates

        # id early exits at invalid digits
        # how are we storing seen values (DS selection)
        # How do you map a coordinate (r, c) to one of the nine 3 x 3 sub-boxes? (Indexing logic)
        # Brute force solution 

        # since we need no duplicates immediate thought is a set()
        # empty boxes use "."
        # could use freq map to track current rows freq of each val 1-9 (if it appears more than once we exit)
        # so for col tracking we do the same on each iteration of a row we are checking a seperate freq map of that col specifically (if we see a val 1-9 occur more than once we exit)
        # freq map of each 3x3 sub-box -- we know we have 9 total
        # we can calulate dynamically in a more complex scenario but in this one we can hard code 3x3 9 times with correct indexes to track freq of entire subbox

        # O(n^2) and O(n^2) space or better
        # Since we know its only vals 1-9 we can use boolean arrays to achieve O(1) space per check instead of using a HashSet<Character> for each row, col and box
        # easier to create 3x3 boxes dynamically / faster
        # rows 0, 1, 2 all belong to the top boxes 
        # columns 0, 1, 2 all belong to the left tier boxes

        #1. The 2D Array vs. HashSet
        #Imagine you have a 2D list called rows_seen = [[False for _ in range(10)] for _ in range(9)].
        #When you are at row r and see digit 5, you check rows_seen[r][5].
        #If it's True, you've seen it in this row before → Invalid!
        #If it's False, you set it to True and keep going.
        #This is O(1) because looking up an index in a list is a direct memory jump.

        #2. Mapping the 3x3 Boxes (The "/ 3" Trick)
        # dont want hard code or bunch of if/else statements - instead its coordinates for the boxes
        # divide row and col by 3 using integer division //
        # rows 0, 1, 2 all become 0 (because 0 //3, 1 //3,2 // 3 all equal 0)
        # rows 3, 4, 5 all become 1
        # rows 6, 7, 8 all become 2
        # same happens for cols 
        # this gives each cell a "box coordinate" (0,0) top left box and (2,2) for the bottom-right box
        # Box ID = (r//3) * 3 + (c //3)

        # if we are at a "." no need to check just pass to next cell to check
        #collections.defaultdict(set) - creates an empty set the first time you try to access a new key. (if you try to add something to a dic key that doesnt exist yet you get a KeyError)

        #"What if the board was 100×100 and the sub-boxes were 10×10?" - (r // 3, c //3) and default dict is highly scalable
        # you just change the 3s to 10s or 100s - range for the loops becomes that val * 3 i believe
       