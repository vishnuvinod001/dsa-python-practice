# Leetcode: 209 - Minimum Size Subarray Sum

def minSubArrayLen(nums, target):
    left = 0
    window_sum = 0
    min_len = float("inf")
    
    for right in range(len(nums)):
        window_sum += nums[right]
        
        while window_sum >= target:
            min_len = min(min_len, right - left + 1)
            window_sum -= nums[left]
            left += 1
    
    return 0 if min_len == float("inf") else min_len

nums = [1,2,3,4,8]
target = 8
print(minSubArrayLen(nums, target))

nums = [2,3,1,2,4,3]
target = 7
print(minSubArrayLen(nums, target))