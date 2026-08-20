* Trie (Prefix Tree) - Quick Notes

    Tree-like data structure used to store strings/words.
    Each node represents a character.
    A path from root to a node represents a prefix.
    Special marker (#, *, is_end) indicates end of a word.

* Operations: 

    Insert(word) → O(n)
    Search(word) → O(n)
    StartsWith(prefix) → O(n)

n = length of the word/prefix

* Why use a Trie?

    Fast prefix lookups.
    Efficient for:
    Autocomplete
    Spell checking
    Dictionary/word search
    Prefix matching problems

* Example

    Words inserted:

    cat
    car
    dog

* Trie

    root
    ├── c
    │   └── a
    │       ├── t*
    │       └── r*
    └── d
        └── o
            └── g*