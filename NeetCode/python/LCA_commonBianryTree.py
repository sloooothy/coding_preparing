# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # ----------------------------------------------------
        # 步驟一：寫出遞迴的終止條件 (Base Case)
        # 思考：
        # 1. 如果 root 是空的 (None)，代表走到盡頭了，該回傳什麼？
        # 2. 如果 root 剛好等於 p 或 q，代表「我找到其中一個目標了！」，
        #    此時直接把 root 回傳上去給上一層，會發生什麼事？
        # ----------------------------------------------------
        if not root or root == p or root == q:
            return root 
            #root 為None => 沒找到
            #root 為 p or q => not None => 有找到節點

        # ----------------------------------------------------
        # 步驟二：分工合作，左右子樹各派人去找
        # 思考：
        # 怎麼呼叫自己去左子樹跟右子樹，並用變數把回傳的結果接住？
        # ----------------------------------------------------
        left_result = self.lowestCommonAncestor(root.left, p, q)
        right_result = self.lowestCommonAncestor(root.right, p, q)

        # ----------------------------------------------------
        # 步驟三：收割成果與判斷交會點 (Combine)
        # 思考：
        # 1. 如果 left_result 和 right_result「同時」都有東西（不為 None），
        #    代表 p 在左邊、q 在右邊（或反過來），那當前的 root 就是交會點！該回傳誰？
        # 2. 如果只有一邊有東西、另一邊是 None，代表 p 和 q 都擠在同一邊，
        #    那該把有東西的那一邊（左或右）往上回傳嗎？
        # 3. 如果兩邊都是 None，代表底下都沒有，該回傳什麼？
        # ----------------------------------------------------
        
        # 填寫你的組合邏輯...
        if left_result and right_result:
            return root
        if left_result and not right_result:
            return left_result #只有左邊有
        if not left_result and right_result:
            return right_result #只有右邊有

        return None
        
        
        
