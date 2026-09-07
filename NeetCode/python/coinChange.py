class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        #建立一個大小為 amount + 1 的陣列 dp。
        #將所有值初始化為一個很大的數字 (例如 float('inf'))，這代表目前還不知道怎麼湊出這個金額。
        dp=[float('inf')]*(amount+1)

        #將 dp[0] 設定為 0。
        dp[0]=0

        #雙層迴圈:
        for i in range(1,amount+1): #外層迴圈遍歷所有可能的金額 i，從 1 到 amount。
            for cc in coins: #內層迴圈遍歷所有可用的硬幣 coin。
                #更新 DP 陣列:
                if i>=cc:#在內層迴圈中，如果 i 大於或等於 coin，那麼你就可以用這枚硬幣來湊出金額 i。
                    #這時候，你可以更新 dp[i]：dp[i] = min(dp[i], dp[i - coin] + 1)。
                    dp[i]=min(dp[i],dp[i-cc]+1) #找使用最少硬幣的解來更新dp[i]

        return -1 if dp[amount]==float('inf') else dp[amount] #沒找到為無限大
