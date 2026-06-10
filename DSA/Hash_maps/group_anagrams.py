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
    