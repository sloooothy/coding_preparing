##
'''
BFS 程式template
'''
##
from collections import deque

def bfs(start_node):
    queue = deque()
    queue.append(start_node)

    while queue:
        level_size = len(queue)  # 取得目前層節點數量，確保分層處理

        for _ in range(level_size):
            node = queue.popleft()

            # 處理當前節點 (如判斷條件、記錄結果等)
            # ...

            # 將子節點加入隊列
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # 這裡可以放「每層結束後要做的事」
