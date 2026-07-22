# Leetcode : 16 - Three Sum Closest
 
 
def threeSumClosest(nums, target):
     
    nums.sort()
    closest = nums[0] + nums[1] + nums[2]
    
    for i in range(len(nums) - 2):
        
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if abs(total - target) < abs(closest - target):
                closest = total
            
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return total
    
    return closest

nums = [-1,2,1,-4]
target = 1
print(threeSumClosest(nums, target))

nums = [0,0,0] 
target = 1
print(threeSumClosest(nums, target))