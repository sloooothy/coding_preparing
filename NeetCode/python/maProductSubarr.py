class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        #初始化：
        #建立兩個變數：max_so_far (追蹤到目前為止的最大乘積) 和 min_so_far (追蹤到目前為止的最小乘積)。
        max_so_far,  min_so_far=nums[0],nums[0]
        #初始值都設為 nums[0]。

        #res 變數來儲存最終結果，也初始化為 nums[0]。
        res=nums[0]

        #迴圈：從第二個元素開始，遍歷整個陣列。
        for i in range(1,len(nums)):
            #對於每一個數字 n，你需要計算三個可能的候選值來更新 max_so_far 和 min_so_far：

            #n (從這個新數字重新開始)
            n=nums[i]
            #n * max_so_far (用當前的最大值乘)
            #n * min_so_far (用當前的最小值乘) #若負負得正
            #在更新 max_so_far 和 min_so_far 時，必須同時使用這三個候選值。
            #為了避免混淆，你可以用一個臨時變數來儲存上一個 max_so_far 的值。
            temp_max_so_far=max(n,max(n*max_so_far,n*min_so_far))
            min_so_far=min(n,min(n*max_so_far,n*min_so_far))
            max_so_far=temp_max_so_far

            #更新結果： 每一次迴圈結束，res 都會被更新成 max(res, max_so_far)，確保我們能捕捉到所有子陣列的最大乘積。
            res=max(res,max_so_far)
            

        return res

        
