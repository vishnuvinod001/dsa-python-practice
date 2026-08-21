Hash Map (Dictionary) — Notes
    - Stores data as key → value pairs.
    - Python implementation: dict.
    - Uses a hash function to quickly locate data.
    - Average O(1) time for:
        * Insert
        * Search
        * Delete
    - Worst case: O(n) (due to collisions, rare).
Common Operations
    - Insert: d[key] = value
    - Access: d[key]
    - Check existence: key in d
    - Delete: del d[key]
    - Get default value: d.get(key, default)
Common DSA Uses
    - Frequency counting
    - Duplicate detection
    - Fast lookups
    - Caching / Memoization
    - Mapping relationships

Intuition
    - Like a labeled drawer system:
    - Key = drawer label
    - Value = item inside
    - Jump directly to the correct drawer instead of searching all drawers.