class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,x):
        self.stack.append(x)
    
    def pop(self):
        if self.isEmpty():
            return "Stack Underflow"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0