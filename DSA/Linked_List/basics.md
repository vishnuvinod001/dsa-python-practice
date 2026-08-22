# Linked Lists

## Basics
- A linked list consists of nodes.
- Each node contains:
  - `val` (data)
  - `next` (pointer to next node)
- Access to the list is through the `head`.

## Common Pointers
- `head` → first node of the list.
- `curr` → current node during traversal.
- `prev` → previous node (used in reversal).
- `fast` → moves 2 steps.
- `slow` → moves 1 step.
- `dummy` → fake head node used to simplify operations.

## Common Patterns

### 1. Traversal
```python
curr = head
while curr:
    curr = curr.next

### 2. Fast & Slow Pointers
Find middle node.
Detect cycles.
Fast moves 2 steps, slow moves 1 step.

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    
