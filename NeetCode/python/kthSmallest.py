# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def dfs(node,list_nodes):

            if(node.left):
                dfs(node.left,list_nodes)
            
            list_nodes.append(node.val)

            if(node.right):
                dfs(node.right,list_nodes)

            if(len(list_nodes)==k):
                return 
            
        nodeList=[]
        dfs(root,nodeList)
        
        return nodeList[k-1]
                

