class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp={len(s):1}

        def dfs(i):
            if i in dp:
                return dp[i]

            # 錯誤處理: 如果當前字元為 '0'，無法獨立解碼，所以解碼方式為 0。
            if s[i] == "0":
                return 0

            res=dfs(i+1)
            if (i+1 <len(s) and 
               (s[i]=="1" or 
               (s[i]=="2" and s[i+1] in "0123456")
               )):
               res+=dfs(i+2)

            # 儲存結果並回傳
            #    將當前子問題的結果存入 dp，以供未來使用
            dp[i] = res
            return res

        return dfs(0) # start from character position = 0 (first char)
            
