import sys


def rob_house(nums):
    n = len(nums)
    if not nums :
        return 0
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    
    def rob_linear(arr):
        prev2 = 0
        prev1 = 0
        for num in arr:
            curr = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = curr
        return prev1
    
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

if __name__ == "__main__":
    nums = list(map(int, sys.argv[1:]))
    print(rob_house(nums))
            
    