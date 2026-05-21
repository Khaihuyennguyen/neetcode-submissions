class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.addWord(w)
        res, visit = set(), set()

        def dfs(node, r, c, subString):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or board[r][c] not in node.children:
                return
            visit.add((r, c))
            node = node.children[board[r][c]]
            subString += board[r][c]
            if node.isWord:
                res.add(subString)
            dfs(node, r + 1, c , subString)
            dfs(node, r - 1, c, subString)
            dfs(node, r, c + 1, subString)
            dfs(node, r, c - 1, subString)


            visit.remove((r,c))

        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                dfs(root, r, c, "")
        return list(res)

        