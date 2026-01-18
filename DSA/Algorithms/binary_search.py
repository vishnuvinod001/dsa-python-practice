import sys

def binary_search(nums, target):
    
    left, right = 0, len(nums) - 1
    
    while left <=right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid-1
    return -1

if __name__ == "__main__":
    nums = list(map(int, sys.argv[1:-1]))
    target = int(sys.argv[-1])
    
    nums.sort()
    print(binary_search(nums, target))