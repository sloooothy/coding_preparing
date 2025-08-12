"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        map_graph={}

        def dfs(node):
            if node in map_graph:
                # 如果有 → 直接回傳 mapping 裡的複製節點。
                return map_graph[node]

            # 如果沒有 → 建立新節點、放到 mapping。
            map_graph[node]=Node(node.val)

            #處理neighbor，每個neighbor都是一個node
            for neighbor in node.neighbors:
                map_graph[node].neighbors.append(dfs(neighbor))

            return map_graph[node] # 回傳這個複製好的節點

        dfs(node)#由最初的node開始dfs巡迴圖
        return map_graph[node] #取出初始node的巡迴結果
