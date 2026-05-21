# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        def visit(node, leftValue, rightValue):
            if not node:
                return True
            if not( node.val < rightValue and node.val > leftValue) :
                return False
            return visit(node.left, leftValue, node.val) and visit(node.right, node.val, rightValue)

        return visit(root, float("-inf"), float("inf"))