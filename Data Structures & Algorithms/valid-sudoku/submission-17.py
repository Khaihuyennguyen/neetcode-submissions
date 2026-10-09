class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(len(rows)):
            for c in range(len(cols)):
                
                num_c = board[r][c]
                if num_c == ".":
                    continue
                num = int(num_c)
                if (1 << num) & rows[r]:
                    return False
                if (1 << num) & cols[c]:
                    return False
                if (1 << num) & squares[r//3 * 3 + c // 3]:
                    return False
                rows[r] |= (1 << num)
                cols[c] |= (1 << num)
                squares[r//3 * 3 + c // 3] |= (1 << num) 

        return True