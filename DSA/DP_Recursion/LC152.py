
# 152. Maximum Product Subarray

def maxProduct(arr):
    currMax = currMin = ans = arr[0]
    
    for i in range(1, len(arr)):
        n = arr[i]
        
        temp = currMax * n
        
        currMax = max(n, currMax * n, currMin * n)
        currMin = min(n, temp, currMin * n)
        
        ans = max(ans, currMax)
    
    return ans


arr = [2,3,-2,4]
print(maxProduct(arr))