class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n=0
        for nn in range(len(nums)+1): # from 0 to N , XOR all the number
            n^=nn

        for i in nums: # XOR the existed number to find the not existed one.
            n^=i

        return n
