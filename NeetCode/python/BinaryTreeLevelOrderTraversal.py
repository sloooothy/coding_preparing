# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        qu=collections.deque()
        qu.append(root)
        while len(qu)>0:
            level=[]
            for i in range(len(qu)):
                cur=qu.popleft()
                if cur:
                    level.append(cur.val)
                    qu.append(cur.left)
                    qu.append(cur.right)
            if len(level)>0:
                res.append(level)

        return res

        



        
