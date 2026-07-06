# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

def subsets(list1):
    list1.sort()
    n = len(list1)
    
    res, sol = [], []
    
    def backtracking(start):
        
        res.append(sol[:])
        
        for i in range(start, n):
            if i > start and list1[i] == list1[i - 1]:   # If in the same level and the numbers are same => skip. 
                                                         # Not the same level => take even if the numbers are same
                continue
            
            sol.append(list1[i])
            backtracking(i + 1)
            sol.pop()
        
    backtracking(0)
    print(res)
    


a = [1, 2, 2, 3]
subsets(a)