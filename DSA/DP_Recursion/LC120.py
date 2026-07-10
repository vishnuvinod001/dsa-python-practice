# LC-120 : Triangle
#    2  
#   3,4
#  6,5,7
# 4,1,8,3

# We want the minimum path : 2 => 3 => 5 => 1 = 11

def minTotal(arr):
    dp = arr[-1][:] # create a copy of the final row
    
    for i in range(len(arr)-2, -1, -1): # start from the second last row (already we have the copy of the last row)
        for j in range(len(arr[i])):
            dp[j] = arr[i][j] + min(dp[j], dp[j+1]) # add the min(left, right) with parent and store at dp[j]

    return dp[0]

arr1 = [[2], [3,4], [5,6,7], [8,9,10,11]] # Expected : 18
print(minTotal(arr1))
arr2 = [[2], [10,5], [56,55,1], [8,9,4,6]] # Expected  : 12
print(minTotal(arr2))