class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        def backtrack(row, cols_used, diag1_used, diag2_used, current_placement):
            if row == n:
                board = ['.' * col + 'Q' + '.' * (n - col - 1) for col in current_placement]
                result.append(board)
            
            for col in range(n):
                if col not in cols_used and (row - col) not in diag1_used and (row+col) not in diag2_used:
                    backtrack(row+1, cols_used | {col}, diag1_used | {row-col}, diag2_used | {row+col}, current_placement + [col])
        
        backtrack(0, set(), set(), set(), [])
        return result