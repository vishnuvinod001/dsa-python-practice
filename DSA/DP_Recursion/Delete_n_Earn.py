import sys

def delEarn(nums):
    if not nums:
        return 0
    max_val = max(nums)
    points = [0]* (max_val+1)
    
    for num in nums:
        points[num] += num
    
    prev2 = 0
    prev1 = points[1]
    
    for i in range(2, max_val+1):
        curr = max(prev1, prev2 + points[i])
        prev2 = prev1
        prev1 = curr
    return prev1


if __name__ == "__main__":
    nums = list(map(int, sys.argv[1:]))
    print(delEarn(nums))

        
"""
        nums = [2,2,3,3,3,4]
        init,points = [0,0,0,0,0] (max_val = 4+1) => no of values
        points = [0,0,4,9,4]

        prev2 = prev1
        prev1 = curr
        curr = max(prev1, prev2 + points[i])
        curr = max(0, 0+4) = 4
        curr = max(4, 0+9) = 9
        curr = max(9, 4+4) = 9
        => 9
    """