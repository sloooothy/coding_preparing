class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]

        rob_1, rob_2 = 0, 0

        # [rob1, rob2, n, n+1 ...]
        # !!!目前在n!!!
        # rob1: 跳過n前一棟房子不搶，要搶n的可累積最大值 (代表到 n 的前兩間房子為止，所能獲得的最大總金額。)
        # rob2: 搶了n前一棟的最大值，因此n不能搶 rob_2保持原狀 (代表到 n 的前一間房子為止，所能獲得的最大總金額。)
        for n in nums:
            temp = max(n + rob_1, rob_2) #目前在n，決定兩個之間誰比較大
            # 為下一個n決定數值
            rob_1 = rob_2 #下一個rob_1用rob_2更新，因為準備要後移了
            rob_2 = temp #目前最大值更新下一個n前一家可獲得最大值
        
        return rob_2
