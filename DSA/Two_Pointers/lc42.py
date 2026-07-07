# LC - 42
# Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

def rainwater(height):
    l_wall, r_wall = 0, 0
    n = len(height)
    max_left = [0] * n
    max_right = [0] * n
    
    for i in range(n):
        j = -i - 1
        max_left[i] = l_wall
        max_right[j] = r_wall
        
        l_wall = max(l_wall, height[i]) # max height from front of the list
        r_wall = max(r_wall, height[j]) # max height from back of the list
        
    summ = 0
    for i in range(n):
        potential = min(max_left[i], max_right[i]) # compare the corresponding elements of the 2 new lists (max_lef, max_right) => this becomes the potential water trapped
        summ += max(0, potential - height[i]) # do this because if potential is 2 but height is 3 => -ve number => we add nothing => 0
    
    return summ  
    
    
a = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output = 6 
print(rainwater(a))