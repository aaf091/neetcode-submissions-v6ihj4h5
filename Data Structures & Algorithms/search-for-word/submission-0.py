class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def dfs(r,c,index):
            if index == len(word)-1:
                return True
            original_char = board[r][c]
            board[r][c] = '#'
            directions = [(-1,0),(1,0),(0,-1),(0,1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == word[index+1]:
                    if dfs(nr, nc, index + 1):
                        return True
                        break
            
            board[r][c] = original_char
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        return False