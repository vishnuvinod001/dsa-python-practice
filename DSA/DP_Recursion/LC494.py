"""
Leetcode: 494 - Target Sum

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

"""

def targetSum(nums, target):
    memo = {}
    
    def dfs(i, total):
        
        if i == len(nums):
            return 1 if total == target else 0

        if (i, total) in memo:
            return memo[(i, total)]
        
        add = dfs(i + 1, total + nums[i])
        subtract = dfs(i + 1, total - nums[i])
        
        memo[(i, total)] = add + subtract
        
        return memo[(i, total)]
    
    return dfs(0, 0)

nums = [1,1,1,1,1]
target = 3

print(targetSum(nums, target)) # Output : 5