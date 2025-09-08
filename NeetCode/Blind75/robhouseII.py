class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        rob1,rob2=0,0

        for money in nums[0:-1]:
            temp=max(money+rob1,rob2)
            rob1=rob2
            rob2=temp

        prefix=rob2

        rob1,rob2=0,0
        for money in nums[1:]:
            temp=max(money+rob1,rob2)
            rob1=rob2
            rob2=temp

        postfix=rob2

        return max(prefix,postfix)
