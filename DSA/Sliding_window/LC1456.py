def maxVowels(s, k):
    
    vowels = {'a', 'e', 'i', 'o', 'u'} # Set with all the vowels
    vowel_count = 0
    
    for i in range(k):              # building the 1st window and its vowel_count
        if s[i] in vowels:
            vowel_count += 1
    
    max_vowels = vowel_count
    
    for i in range(k, len(s)):
        if s[i] in vowels:          # If the LATEST letter is a vowel.
            vowel_count += 1
        
        if s[i - k] in vowels:      # if the REMOVED letter is a vowel
            vowel_count -= 1
        
        max_vowels = max(max_vowels, vowel_count)
        
    return max_vowels

s = "aaaiubaaeeiio"
k = 5
print(maxVowels(s, k))

s = "abciiidef"
k = 3
print(maxVowels(s, k))