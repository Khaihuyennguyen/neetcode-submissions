class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
      
        bottomRow = [1] * COLS

        for col in range(ROWS - 1):
            newRow = [1] * COLS

            for row in range(COLS - 2, -1, -1):
                newRow[row] = bottomRow[row] + newRow[row + 1] # sum of row bellow and row next to it
            bottomRow = newRow
        return bottomRow[0]



