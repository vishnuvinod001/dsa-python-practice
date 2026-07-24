# Leetcode: 1498 - Number of subsequences that satisfy the given sum condition
# Here in a subsequence the sum of MIN and MAX needs to be <+ target.

def numSubseq(nums, target):
    
    MOD = 10 ** 9 + 7
    n = len(nums)
    nums.sort()
    powers = [1] * n
    
    for i in range(1, n):
        powers[i] = (powers[i - 1] * 2) % MOD
    
    left = 0
    right = n - 1
    
    count = 0
    
    while left <= right:
        if nums[left] + nums[right] <= target:
            count += powers[right - left]
            count %= MOD

            left += 1
        
        else:
            right -= 1
    
    return count

nums = [3,5,6,7]
target = 9
print(numSubseq(nums, target))

# output: 4 - [3], [3,5], [3,5,6], [3,6]
"""
MOD is used to normalize the COUNT variable as it can get enormous in exponents.
This is given in the Qn.
1_000_000_007 - This will be the value. this only applies if the numbers which are modded with this exceeds this exact number.
"""