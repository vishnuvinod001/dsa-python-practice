"""
LeetCode 1 - Two Sum

Approach:
- Store previously seen numbers in a hashmap.
- For each number, check if its complement exists.
- Return indices when found.

Time: O(n)
Space: O(n)
"""

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    
    for i, num in enumerate(nums):
        needed = target - num
        
        if needed in seen:
            return(seen[needed],i)
        
        seen[num] = i
        
    return []

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    
    print(two_sum(nums, target))