# Longest Palindromic Substring
# ababa, abba, abbabba

def longestPalindrome(s:str):
    if not s:
        return ""
    
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l -1
    
    start, end = 0, 0
    for i in range(len(s)):
        len1 = expand(i, i) # odd len string
        len2 = expand(i, i+1) # even len string
        
        length = max(len1, len2)
        
        if length > end - start:
            start = i - (length - 1) // 2 
            end = i + length // 2
    
    return s[start: end + 1]

strList = ["cabbabbad", "dabaf", "abbabba", "abcdc" ]

for s in strList:
    print(longestPalindrome(s))