def main():
    visited = set() #避免重複訪問，用set維護已處理

    def helper(node): #helper function
        if not node or node in visited:
            return
        visited.add(node) #加入已處理節點

        # 處理
        # ...

        for nei in node.neighbors:
            helper(nei)

    helper(start_node)
