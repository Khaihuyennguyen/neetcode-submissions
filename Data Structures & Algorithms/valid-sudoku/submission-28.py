class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(len(rows)):
            for c in range(len(cols)):
                value = board[r][c]
                if value == ".":
                    continue
                
                value = int(value)
                if (1 << value) & rows[r]:
                    return False
                if (1 << value) & cols[c]:
                    return False
                if (1 << value) & squares[r // 3 * 3 + c // 3]:
                    return False

                rows[r] |= (1 << value)
                cols[c] |= (1 << value)
                squares[r // 3 * 3 + c // 3] |= (1 << value)
            
        return True
