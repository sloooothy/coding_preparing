# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        #準備一個籃子和一個筆記本：
        basket=deque()
        notebook=[]
        res=[]
        #首先，把樹的「樹幹」（根節點 root）放進你的籃子裡。
        basket.append(root)
        
        #只要籃子裡還有東西，我們就繼續處理：
        while(basket):
            #計數： 數一下現在籃子裡有多少個節點。這些節點就是「當前這一層」的所有節點。
            cnt_layer=len(basket)
            #清空籃子，記錄本層：
            layer=[] #準備一張新的紙（一個新的列表），用來寫下這一層的節點值。
            for i in range(cnt_layer):
                #把籃子裡的每個節點一個一個地拿出來。
                curNode=basket.popleft()
                #每拿出來一個節點：
                #把它的「值」寫到這張新紙上。
                layer.append(curNode.val)
                #如果這個節點有「左邊小孩」（左子節點），就把左邊小孩放進籃子裡。
                if(curNode.left):
                    basket.append(curNode.left)
                #如果這個節點有「右邊小孩」（右子節點），就把右邊小孩放進籃子裡。
                if(curNode.right):
                    basket.append(curNode.right)

            #記下這層： 把這張寫滿了當前這層節點值的新紙，放到你的大筆記本裡。
            res.append(layer)

        return res


