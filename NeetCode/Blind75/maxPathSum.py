# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum=float('-inf') #初始化為一個非常小的負數，這樣才能正確處理所有節點都是負數的情況

        def helper_findMax(root):
            nonlocal maxSum #要先註記要更新的是global變數
            if root==None:
                return 0
                
            leftSum = max(0, helper_findMax(root.left))
            rightSum = max(0, helper_findMax(root.right))

            maxSum =max(maxSum,root.val+leftSum+rightSum) #更新global變數
            
            return root.val+max(leftSum,rightSum) #回報目前節點的maxSum

        helper_findMax(root)

        return maxSum
