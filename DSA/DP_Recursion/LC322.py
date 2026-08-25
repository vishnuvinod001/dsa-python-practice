"""
Leetcode: 322 - Coin Change

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

"""

def coinChange(coins, amount):
    
    dp = [float('inf')] * (amount + 1)
    
    dp[0] = 0
    
    for amt in range(1, amount + 1):
        for coin in coins:
            if amt - coin >= 0:
                dp[amt] = min(dp[amt], 1 + dp[amt - coin])  # Multiple ways to make the amount, we take the minimum number of coins needed
    
    return dp[amount] if dp[amount] != float('inf') else -1

coins = [1,2,5]
amount = 11

print(coinChange(coins, amount)) # Output : 3

coins = [2]
amount = 3
print(coinChange(coins, amount)) # Output : -1

coins = [1]
amount = 0
print(coinChange(coins, amount)) # Output : 0