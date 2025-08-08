# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        preorder_str=""
        def preorder_dfs(node):
            nonlocal preorder_str
            if(node!=None):
                preorder_str+=""+str(node.val)+","
                preorder_dfs(node.left)
                preorder_dfs(node.right)
            else:
                preorder_str+="null,"
            

        preorder_dfs(root)

        return preorder_str[:-1]
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data_res=data.split(",")
        self.i = 0 #global variable, counting node position

        def dfs():
            if data_res[self.i] == "null": # null node
                self.i += 1
                return None
            node = TreeNode(int(data_res[self.i])) #regular node
            self.i += 1
            #constructing the children
            node.left = dfs()
            node.right = dfs()
            return node #compelete constructing children, return the whole node

        return dfs()
