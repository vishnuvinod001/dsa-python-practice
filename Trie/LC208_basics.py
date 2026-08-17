class Trie:
    
    def __init__ (self):
        
        self.trie = {}
    
    def insert(self, word):
        
        d = self.trie

        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        
        d['.'] = '.'
        
    def search(self, word):
        
        d = self.trie
        
        for c in word:
            if c not in d:      # Character not in the dictionary, word not found
                return False
            d = d[c]        # Get deep into the dictionary (nested dictionary)
        
        return '.' in d
    
    def startsWith(self, prefix):
        
        d =self.trie
        
        for c in prefix:
            if c not in d:      # Character not in the dictionary, prefix not found
                return False
            d = d[c]        # Get deep into the dictionary (nested dictionary)
        
        return True