# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, lower_bound, upper_bound):
            lb = lower_bound
            ub = upper_bound

            if not node:
                return True
            
            if not (lb < node.val < ub):
                return False
            
            left_valid = validate(node.left, lb, node.val)
            if left_valid:
                right_valid = validate(node.right, node.val, ub)
            else:
                right_valid = False
            return left_valid and right_valid

        return validate(root, float("-inf"), float("inf"))
