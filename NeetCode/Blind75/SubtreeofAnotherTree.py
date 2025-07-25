# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p,q):
            if not p and not q:
                return True
            if (not p and q) or (not q and p):
                return False
            if p and q and p.val==q.val:
                return isSameTree(p.left,q.left) and isSameTree(p.right,q.right) 
            else:
                return False
        
        if not subRoot: #如果「小孫樹」本身就是空的（沒有樹幹），那它是不是可以被認為是任何一棵樹的「子樹」呢？
            return True
        
        if not root and subRoot: #如果「阿公樹」本身是空的，但「小孫樹」不是空的，那小孫樹當然不可能成為阿公樹的子樹
            return False

        if root and subRoot:
            if isSameTree(root,subRoot): #直接比對阿公樹的「樹幹」跟小孫樹是否一模一樣？
                return True
            else: #如果樹幹不一樣 那就換比阿公樹的「左分枝」或 「右分枝」
                return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
