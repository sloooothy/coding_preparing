class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(r, c):
            # 邊界條件
            if r < 0 or r >= n or c < 0 or c >= m:
                return
            # 遇水或已訪問則返回
            if grid[r][c] == '0':
                return

            # 標記這格為已訪問（變成水）
            grid[r][c] = '0'

            # 往四個方向繼續探索
            dfs(r - 1, c)  # 上
            dfs(r + 1, c)  # 下
            dfs(r, c - 1)  # 左
            dfs(r, c + 1)  # 右


        # dimension       
        n=len(grid)
        m=len(grid[0])

        cnt_island=0

        for r in range(n):
            for c in range(m):
                if grid[r][c]=="0":
                    continue
                else:
                    cnt_island+=1
                    dfs(r, c)

        return cnt_island
