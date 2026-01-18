from basics import TreeNode

def inOrd(root): # root -> left -> right
    res = []
    
    def dfs(node):
        if not node:
            return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return res

def preOrd(root): # left -> root -> right
    res = []
    
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)
        
    dfs(root)
    return res

def postOrd(root):
    res = []
    
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        res.append(node.val)
        
    dfs(root)
    return res
        
    
