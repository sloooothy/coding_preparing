class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset={} # set to keep nums's element and position
        for i,n in enumerate(nums):
            diff=target-n # the remain value
            if diff in hashset: # if the remain value was lay in previous position
                return [hashset[diff],i] # return the previous position and current position
                
            hashset[n]=i #if not, keep the position record for current number
