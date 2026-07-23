# Leetcode: 18 - 4Sum

def fourSum(nums, target):
    
    nums.sort()
    ans = []
    n = len(nums)
    
    for i in range(n - 3):
        
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        for j in range(i + 1, n - 2):
            
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            
            left = j + 1
            right = n - 1
            
            while left < right:
                
                total = nums[i] + nums[j] + nums[left] + nums[right]
                
                if total < target: # need a bigger target => increment left
                    left += 1
                elif total > target: # need a smaller target => decrement right
                    right -= 1
                else:
                    ans.append([nums[i], nums[j], nums[left], nums[right]])
                    
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]: # previous element to right was in (right + 1)
                        right -= 1
    return ans

nums = [1, 2, 3, 4, 0, 0, 0, 5, 6, 2]
target = 8
print(fourSum(nums, target))

nums = [1,2,3,4,5,6,7,0,0,0,0,0]
target = 8
print(fourSum(nums, target))