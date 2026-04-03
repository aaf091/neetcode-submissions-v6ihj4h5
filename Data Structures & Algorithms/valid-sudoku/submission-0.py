class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set) # Key: (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                
                # Check if number already in row, column, or 3x3 box
                if (num in rows[r] or
                    num in cols[c] or
                    num in boxes[(r // 3, c // 3)]):
                    return False
                
                # Add number to sets
                rows[r].add(num)
                cols[c].add(num)
                boxes[(r // 3, c // 3)].add(num)
                
        return True
            