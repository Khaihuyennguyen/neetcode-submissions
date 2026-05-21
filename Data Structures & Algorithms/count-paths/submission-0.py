class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row, col = m, n

        newBottomRow = [1] * col

        for r in range(row - 1):
            newRow = [1] * col
            for c in range(col - 2, -1, -1):
                newRow[c] = newRow[c + 1] + newBottomRow[c]
            newBottomRow = newRow
        return newBottomRow[0]
