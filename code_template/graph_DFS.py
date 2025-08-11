def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)

    # 處理節點
    # ...

    for nei in node.neighbors:
        dfs(nei, visited)
