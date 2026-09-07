class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]

        def dfs(i,curs,total):
            if total==target:
                res.append(curs.copy())
                return

            if i>=len(nums) or total > target: # selected candidate is over the range of nums (no more candidate)
                return 

            curs.append(nums[i]) # select current nums in curs
            dfs(i,curs,total+nums[i]) # check if we use same candidate is okay
            curs.pop() # pop previous one 
            dfs(i+1,curs,total) # to next candidate

        dfs(0,[],0) # initial state
        return res




