class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n

        bottomRow = [1] * COLS

        for i in range(ROWS - 1):
            newRow = [1] * COLS
            for j in range(COLS - 2, -1, -1):
                newRow[j] = newRow[j + 1] + bottomRow[j]
            bottomRow = newRow
        return bottomRow[0]

