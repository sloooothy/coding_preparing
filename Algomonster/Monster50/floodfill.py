def flood_fill(r: int, c: int, replacement: int, image: list[list[int]]) -> list[list[int]]:
    targetNum=image[r][c]
    ROWS,COLS=len(image),len(image[0])

    def dfs(r, c, t, rp):
        if t==rp:#不須替換的場合
            return 
        # 邊界條件 or # 已變成replacement (r)
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or image[r][c]==rp or (image[r][c]!=t and image[r][c]!=rp):
            return
        # 標記這格為已訪問
        if image[r][c] == t:
            image[r][c] = rp
            
        # 往四個方向繼續探索
        dfs(r - 1, c, t, rp)  # 上
        dfs(r + 1, c, t, rp)  # 下
        dfs(r, c - 1, t, rp)  # 左
        dfs(r, c + 1, t, rp)  # 右

    dfs(r, c, targetNum, replacement)

    return image
