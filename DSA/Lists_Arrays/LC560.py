# Subarray Sum Equals K
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals k.

def subarraySum(nums, k):
    
    prefix_sum = 0
    count = 0
    prefix_count = {0: 1}
    
    for num in nums:
        prefix_sum += num
        
        if prefix_sum - k in prefix_count:
            count += prefix_count[prefix_sum - k]
            
        
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
    
    return count

nums = [1,1,1]
k = 2

print(subarraySum(nums, k)) # 2 [1,1], [1,1]

nums = [1,2,3]
k = 3

print(subarraySum(nums, k)) # 2 [1,2], [3]