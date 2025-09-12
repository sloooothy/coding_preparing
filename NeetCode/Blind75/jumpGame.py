class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        #初始化：
        #創建一個變數 max_reach，代表目前能跳到的最遠距離。初始值是 0。
        max_reach=0

        #遍歷陣列：
        #使用一個迴圈，從索引 i = 0 開始，一直到最後一個可達的索引。
        for i in range(len(nums)):
            #檢查是否卡住：
            #記得，如果在迴圈的任何時候，當前的索引 i 超過了 max_reach，這代表你已經無法再前進了。這時候，直接回傳 False。
            if i>max_reach:
                return False

            #核心邏輯：
            max_reach=max(max_reach,i+nums[i])#這代表從 i 這一格，最遠能跳到 i + nums[i]，所以我們用它來更新最遠可達的距離。
            
        #回傳結果：
        #如果迴圈順利結束，代表你沒有卡住，最後只需檢查 max_reach 是否能覆蓋到終點。
        return True


        
        

        
