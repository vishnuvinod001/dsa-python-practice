# Leetcode: 15 - Three Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# ==> Sum from different indices.

def threeSum(nums):
    
    nums.sort()
    ans = []
    
    for i in range(len(nums) - 2):
        
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            
            total = nums[i] + nums[left] + nums[right]
            
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                ans.append([nums[i], nums[left], nums[right]])
                
                left += 1
                right -= 1
                
                while left < right and nums[left] == nums[left - 1]: # duplicate left
                    left += 1
                while left < right and nums[right] == nums[right + 1]: # duplicate right
                    right -= 1
    
    return ans

nums = [-1, 2, -2, 0, 1, -4, 2]
print(threeSum(nums))
nums = [-1, 1, 0, 2, -2, 0, 2, 2, -4]
print(threeSum(nums))