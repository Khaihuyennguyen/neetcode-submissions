class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we create a ds that can check if a number is duplicate
        # for each element, we check that col row and box

        hash_rows = collections.defaultdict(set)
        hash_cols = collections.defaultdict(set)
        hash_box = collections.defaultdict(set) # the key is (r//3 c //3)

        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                if board[r][c] in hash_rows[r] or board[r][c] in hash_cols[c] or board[r][c] in hash_box[(r//3, c//3)]:
                    return False

                hash_rows[r].add(board[r][c])
                hash_cols[c].add(board[r][c])
                hash_box[(r//3,c//3)].add(board[r][c])

        return True