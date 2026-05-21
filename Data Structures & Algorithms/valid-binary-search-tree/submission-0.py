# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        if not root: return True

        def visit(leftValue, current, rightValue):
            if not current: return True
            if not (current.val > leftValue and current.val < rightValue):
                return False
            return visit( leftValue , current.left, current.val) and visit(current.val, current.right, rightValue)
        return visit(float("-inf"), root, float("inf"))
