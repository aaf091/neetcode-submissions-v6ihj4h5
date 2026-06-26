class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        if not matrix or not matrix[0]:
            return False
        # Find the row which contains the target
        L,R = 0,m*n-1
        while L<=R:
            M=(L+R)//2
            row=M//n
            col=M%n
            current_value = matrix[row][col]
            if current_value == target:
                return True
            elif current_value > target:
                R=M-1
            else:
                L=M+1
        return False
