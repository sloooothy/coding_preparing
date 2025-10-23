class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {} # 用於「記憶化」儲存子問題的結果，避免重複計算 (key 是起始索引 i)
        
        def dfs(i):
            if i == len(s):
                return True # 終止條件：索引到達字串結尾，表示成功拆分完畢

            # Step 2: Check if result is already in memo
            if i in memo:
                return memo[i] # 如果已計算過 i 這個子問題，直接回傳結果

            for w in wordDict: # 嘗試用字典中的每個單詞 w 來匹配
                if ((i + len(w)) <= len(s) and # 檢查 w 的長度是否超出字串範圍
                     s[i : i + len(w)] == w # 檢查 s[i...] 是否以 w 開頭
                ):
                    if dfs(i + len(w)): # 遞迴：若成功匹配 w，則檢查剩餘部分 (從 i + len(w) 開始)
                        # Step 3a: Store result before returning True
                        memo[i] = True # 記錄從 i 開始的拆分是成功的
                        return True # 找到一條成功路徑，立即回傳

            # Step 3b: Store result before returning False
            memo[i] = False # 嘗試完所有單詞 w 都失敗，記錄從 i 開始的拆分是失敗的
            return False # 回傳失敗

        return dfs(0) # 從字串的起始位置 (索引 0) 開始進行 DFS 拆分
