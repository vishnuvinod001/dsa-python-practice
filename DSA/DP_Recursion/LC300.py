
'''
300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest
strictly increasing subsequence.

'''

def lengthofLIS(nums):
    
    n = len(nums)
    dp = [1] * n
    
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

nums = [10,9,2,5,3,7,101,18]
print(lengthofLIS(nums))

nums = [0,1,0,3,2,3]
print(lengthofLIS(nums))