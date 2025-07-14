class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs_depth(root):

            if root==None:
                return 0

            return max(dfs_depth(root.left),dfs_depth(root.right))+1

        return dfs_depth(root)
