
def minDistance(word1, word2):
    """
    for i in range(m + 1):
        dp[i][n] = m - i
        # word2 is exausted, so delete the remaining chars from word1
    """
    """
    for j in range(n + 1):
        dp[m][j] = n - j
        # word1 is exhausted, so we add the remaining chars from word2
    """
    """
    dp[i][j] = 1 + min(
                    dp[i + 1][j + 1], # Replace
                    dp[i + 1][j], # Delete
                    dp[i][j + 1] # Insert
                )
    """
    
    m, n = len(word1), len(word2)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][n] = m - i
    
    for j in range(n + 1):
        dp[m][j] = n - j
        
    for i in range(m - 1, -1, -1):
        
        for j in range(n - 1, -1, -1):
            
            if word1[i] == word2[j]:
                dp[i][j] = dp[i + 1][j + 1]
                
            else:
                dp[i][j] = 1 + min(
                    dp[i + 1][j + 1],
                    dp[i + 1][j],
                    dp[i][j + 1]
                )
    return dp[0][0]

word1 = "horse"
word2 = "ros"
print(minDistance(word1, word2)) # Output: 3

"""
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
"""