class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [0] * 9
        rows = [0] * 9
        squares = [0] * 9


        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                num = int(num)
                if (1 << num) & cols[c]:
                    return False
                if (1 << num) & rows[r]:
                    return False
                if (1 << num) & squares[r // 3 * 3 + c // 3]:
                    return False

                rows[r] |= (1 << num)
                cols[c] |= (1 << num)
                squares[r // 3 * 3 + c // 3] |= (1 << num) 

        return True