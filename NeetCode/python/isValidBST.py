# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, min_val, max_val):
            # ----------------------------------------------------
            # 提示一：基礎出口 (Base Case)
            # 思考：如果當前的 root 已經是空節點 (None) 了，
            # 代表這條路安然通過、沒有違規，這時候該回傳什麼？
            # ----------------------------------------------------
            if not root:
                return True
            # ----------------------------------------------------
            # 提示二：嚴格審查當前節點 (Validation)
            # 思考：站在當前節點，它的數值 (root.val) 有沒有乖乖被夾在
            # 「大於 min_val」且「小於 max_val」的範圍裡？
            # 如果超過了這個範圍，代表這不是合法的 BST，該回傳什麼？
            # ----------------------------------------------------
            # 2. 審查當前節點（如果 min_val 或 max_val 不是 None，才進行嚴格檢查）

            if root.val <= min_val or root.val>=max_val: 
                return False

            # ----------------------------------------------------
            # 提示三：分工交辦並把「生存區間」往下傳 (Recursive Step)
            # 思考：
            # 1. 準備往左子樹走時：上限 (max_val) 要變成誰？下限要保持不動嗎？
            # 2. 準備往右子樹走時：下限 (min_val) 要變成誰？上限要保持不動嗎？
            # 3. 左右兩邊的檢查結果要用什麼邏輯結合（and 還是 or）？
            # ----------------------------------------------------
            # (在這裡寫你的左右遞迴與結果回傳...)
            return dfs(root.left, min_val, root.val) and dfs(root.right, root.val, max_val)

        return dfs(root,-float('inf'),float('inf'))
                    


        
