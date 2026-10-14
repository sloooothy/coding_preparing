# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        qn=[] #queue of sorted elements

        def dfs(root):
            if not root:
                return 
                
            dfs(root.left)

            if len(qn)<k:
                qn.append(root.val)

            
            dfs(root.right)

        dfs(root)
        return qn[-1]


        
            
        
