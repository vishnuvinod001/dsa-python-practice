"""

Leetcode: 69 - Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

"""

def sqrt(x):
    l, r = 0, x
    
    while l <= r:
        
        m = (l + r) // 2
        m_sq = m * m
        
        if m_sq == x:
            return m
        
        elif m_sq < x:
            l = m + 1
            
        else:
            r = m - 1
    
    return r

print(sqrt(8))
print(sqrt(36))
print(sqrt(25))