# Leetcode: 3 - Longest Substring Without Repeating Characters

def longestSubString(s):
    l = 0
    n = len(s)
    longest = 0
    sett = set()
    
    for r in range(n):
        while s[r] in sett:
            sett.remove(s[l])
            l += 1
        
        w = (r - l) + 1
        longest = max(longest, w)
        sett.add(s[r])
    
    return longest

s = "abbcbadbab"
print(longestSubString(s))
s = "abcabcbb"  
print(longestSubString(s))  