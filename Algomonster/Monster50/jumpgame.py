def jump_game(nums: list[int]) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    maxStep=nums[0]
    for i in range(len(nums)):
        if maxStep<i:
            return False
        maxStep= max(maxStep, i + nums[i])

        if  maxStep >= len(nums) - 1:
            return True
    
    return maxStep >= len(nums) - 1
