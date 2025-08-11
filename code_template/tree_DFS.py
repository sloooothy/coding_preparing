def dfs(node):
    if not node: # None 走到空節點
        return

    # 處理目前節點（例如訪問、計數、判斷）
    # ...

    # 遞迴訪問子節點
    if node.left:
        dfs(node.left)
    if node.right:
        dfs(node.right)
