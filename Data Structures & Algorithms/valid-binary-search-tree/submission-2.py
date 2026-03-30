# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, lb, ub):

            if not node:
                return True
            
            if not (lb < node.val < ub):
                return False

            return validate(node.left, lb, node.val) and validate(node.right, node.val, ub)

        return validate(root, float("-inf"), float("inf"))
