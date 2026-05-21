# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        maxSum = float("-inf")
        def visit(node):
            if not node: return 0
            leftSum = visit(node.left)
            rightSum = visit(node.right)
            nonlocal maxSum
            maxSum = max(leftSum + rightSum + node.val, maxSum)

            return max(leftSum + node.val, rightSum + node.val, 0)
        visit(root)
        return maxSum

