"""
LeetCode 49 - Group Anagrams

Approach:
- Sort each word.
- Use sorted word as hashmap key.
- Group words with same sorted form.

Time: O(n * k log k)
Space: O(n * k)

where:
n = number of strings
k = average string length
"""

from typing import List

def group_anagrams(words: List[str]) -> List[List[str]]:
    anagrams = {}
    
    for word in words:
        sorted_word = tuple(sorted(word))
        
        if sorted_word not in anagrams:
            anagrams[sorted_word] = []
            
        anagrams[sorted_word].append(word)
    return list(anagrams.values())

if __name__ == "__main__":
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(words))
    