# Leetcode: 643 - Maximum Average Subarray - 1

def findMaxAverage(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    for i in range(k, len(nums)):
        window_sum += nums[i]
        window_sum -= nums[i - k]
        
        max_sum = max(max_sum, window_sum)
        
    return max_sum / k

nums = [1,12,-5,-6,50,3]
k = 4

print(findMaxAverage(nums, k))