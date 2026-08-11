"""
you are standing at the bottom of a staircase with n stairs.

at each step you can climb 1 stp or 2 steps

Qn - In how many distinct ways can you reach the top? 


Solution:
    lets say we are at step n: how could you have reached there?
        from step n-1, by taking 1 step
        from step n-2, by taking 2 steps
        
    => the no. of ways to reach step n:
    
        ways(n) = ways(n-1) + ways(n-2) --> Heart of the problem 
    
    ! Recursion:
        Number of ways to reaach n = ways to reach (n-1) + ways to reach (n-2)
        
        Base Cases:
            n = 0; 1 way  => do nothing
            n = 1; 1 way  => 1 step
              
"""

"""
#! Recursion
import sys
    
def climb(n):
    if n == 0 or n == 1:
        return 1
    return climb(n-1) + climb(n-2)

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(climb(n))

#=> Massive Recomputation, Exponential time - O(2^n)    
"""


"""
#! Memoization (Top - Down)

import sys

def climb(n, dp = None):
    if dp is None:
        dp = {}
    if n == 0 or n == 1:
        return 1
    
    if n in dp:
        return dp[n]
    
    dp[n] = climb(n-1, dp) + climb(n-2, dp)
    return dp[n] 

if __name__ == "__main__":
    n = int(sys.argv[1])  # get argument form terminal
    print(climb(n))

"""

"""
#! Tabulation (Bottom - Up DP)
import sys

def climb(n):
    dp = [0]* (n+1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[i]
    
if __name__ == "__main__":
    n = int(sys.argv[1])
    print(climb(n))
"""




#! Space optimized DP

import sys

def climb(n):
    if n == 0 or n == 1:
        return 1
    
    prev2 = 1 # dp[i-2]
    prev1 = 1 # dp[i-1]
    
    for i in range(2, n+1):
        cur = prev1 + prev2
        prev2, prev1 = prev1, cur
    
    return prev1
    

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(climb(n))





