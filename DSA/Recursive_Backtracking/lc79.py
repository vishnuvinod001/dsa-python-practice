# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.


def subsets(list1):
    n = len(list1)
    res, sol = [], []
    
    def backtracking(i):
        
        if i == n:
            res.append(sol[:])
            return
        
        # Don't pick the current list1[i] 
        backtracking(i+1)
        
        # Pick the current list1[i]
        sol.append(list1[i])
        backtracking(i+1)
        sol.pop()
    
    backtracking(0)
    print(res)


a = [1, 2, 3]
subsets(a)        