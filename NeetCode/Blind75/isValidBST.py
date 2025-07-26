# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def chk_valid(curNode,leftbound,rightbound):
            if not curNode:
                return True

            if curNode.val > leftbound and curNode.val<rightbound: #valid，進一步限縮
                # 給「左邊小孩」: 不能大於爸媽，rightbound 更新
                # 給「右邊小孩」: 不能小於爸媽，leftbound 更新
                return chk_valid(curNode.left, leftbound, curNode.val) and chk_valid(curNode.right, curNode.val, rightbound)
            else:
                return False


        #當你檢查大家長的時候，它上面沒有人管它，所以它的值沒有上限也沒有下限。就好像可以從「很小很小的數字」到「很大很大的數字」都可以。
        return chk_valid(root,-float('inf'),float('inf'))
