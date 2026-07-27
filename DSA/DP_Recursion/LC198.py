import sys

def rob(nums):
    n = len(nums)
    dp = {}
    
    def solve(i):
        if i  < 0:
            return 0
        if i in dp:
            return dp[i]
        dp[i] = max(solve(i-1), nums[i] + solve(i-2))
        
        return dp[i]
    return solve(n-1)

if __name__ == '__main__':
    nums = list(map(int, sys.argv[1:]))
    print(rob(nums))
            
    



"""
#! Memoization (Top - Down DP)
import sys

def rob(nums):
    n = len(nums)
    dp = {}
    
    def solve(i):
        if i < 0:
            return 0
        if i in dp:
            return dp[i]
        dp[i] = max(solve(i-1), nums[i] + solve(i-2))
        return dp[i]
        
    return solve(n-1)
    
if __name__ == "__main__":
    nums = list(map(int, sys.argv[1:]))
    print(rob(nums))
    
"""

"""
#! Space Optimized DP

import sys
def rob(nums):
    prev2 = 0
    prev1 = 0
    
    for money in nums:
        cur = max(prev1, prev2 + money)
        prev2 = prev1    # i-2
        prev1 = cur      # i-1
        
    return prev1

if __name__ == '__main__':
    nums = list(map(int, sys.argv[1:]))
    print(rob(nums))

"""

    