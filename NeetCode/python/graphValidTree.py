class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # 1. 建立圖的鄰接表
        graph = {i: [] for i in range(n)}
        for [u,v] in edges:
            graph[u].append(v)
            graph[v].append(u)

        # 2. 追蹤已拜訪的節點
        visited = set()
        
        # 3. 實作 DFS 遞迴函式
        # cur: 目前的節點, prev: 父節點
        def dfs(cur, prev):
            visited.add(cur)

            # 遞迴拜訪所有相鄰的節點
            for adjNode in graph[cur]:
                if adjNode == prev: # 如果鄰居是父節點(回頭路)，就跳過
                    continue
                
                # 不是父節點，則開始選擇路徑
                # 情況 A: 發現新的未拜訪的節點，以cur當父節點繼續遞迴
                if adjNode not in visited:
                    if not dfs(adjNode, cur): # 遞迴呼叫
                        return False
                # 情況 B: 發現一個已拜訪的節點(adjNode in visited)，代表有環
                else:
                    return False
            
            #所有節點確定沒有環
            return True

        # 4. 從節點 0 開始進行 DFS 遍歷 & 檢查連通性：確認所有節點都已被拜訪過
        # 如果 DFS 回傳 False，代表有環，則直接回傳 False
        # 如果 visited 的大小不等於節點總數 n，代表圖不連通
        return dfs(0, -1) and len(visited) == n
