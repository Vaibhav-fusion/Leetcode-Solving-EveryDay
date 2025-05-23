# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        check=float("inf")

        def dfs(root,low,high):
            if root is None:
                return True

            if not (low<root.val<high):
                return False

            return dfs(root.left,low,root.val) and  dfs(root.right,root.val,high)

        return dfs(root,float('-inf'),float('inf'))


            

        
