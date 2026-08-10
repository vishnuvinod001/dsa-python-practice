def removeStars(s):
    stack1 = []
    
    for i in s:
        if i != "*":
            stack1.append(i)
        else:
            stack1.pop()
    
    return "".join(stack1)

s = "leet**cod*e"
print(removeStars(s))  # Output: "lecoe"