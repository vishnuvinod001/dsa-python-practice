"""
Leetcode - 518. Coin Change II
Medium
Topics
premium lock icon
Companies
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.
"""

def maxChange(coins, amount):
    
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for coin in coins:
        for amt in range(coin, amount + 1):   # Because the permutations to that particular coin has already been calculated in the parent loop.
            dp[amt] += dp[amt - coin]
            
    return dp[amount]


amount = 5
coins = [1,2,5]
print(maxChange(coins, amount))