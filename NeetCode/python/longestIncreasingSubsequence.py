class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N=len(nums)
        dp=[1]*N #以位置i 為increase array最後一個元素的最長長度

        for i in range(N):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
        #print(dp)
        return max(dp)
