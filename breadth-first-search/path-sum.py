# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self,node,target):
        if node==None:
            return False
        target-=node.val
        if node.left==None and node.right==None:
            return target==0
        return self.dfs(node.left,target) or self.dfs(node.right,target)

        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs(root,targetSum)

        