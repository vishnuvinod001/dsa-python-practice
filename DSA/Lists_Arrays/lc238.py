# Leetcode: 238 - Product of array except self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# [1,2,3,4] => [24,12,8,6]

def productExceptSelf(nums):
    
    l_mult = 1
    r_mult = 1
    
    n = len(nums)
    l_arr =[0] * n
    r_arr = [0] * n
    
    for i in range(n):
        
        j = -i -1
        l_arr[i] = l_mult
        r_arr[j] = r_mult
        
        l_mult *= nums[i]
        r_mult *= nums[j]
        
    return [l*r for l, r in zip(l_arr, r_arr)]


a = [1,2,3,4]
print(productExceptSelf(a))

# Create 2 arrays with the products from both ends
# 1 [1,2,3,4] 1

# l_arr => add 1,| 1*1 => add 1,| 1*2 => add 2,| 2*3 => add 6,| 6*4 => out of bound|
# r_arr => add 1, | 1*4 => add 4,| 4*3 => add 12,| 12*2 => add 24,| 24*1 => out of bound  ====> This is in reverse

# l_arr = [1, 1, 2, 6] - out_of_bound
# r_arr = [24, 12, 4, 1 ] - out_of_bound
# multiply element wise
# => [24, 12, 8, 6]


