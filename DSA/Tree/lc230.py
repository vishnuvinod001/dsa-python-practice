# LC:230 - Kth Smallest Element in a BST

def kthSmallest(self, root, k):
    self.count = 0
    self.ans = None
    
    def inorder(node):
        # Code to stop the look up and loop after finding the answer
        if not node or self.ans is not None:
            return
        
        inorder(node.left)
        
        self.count += 1
        if self.count == k:
            self.ans = node.val
            return 

        inorder(node.right)
        
    inorder(root)
    return self.ans

# DO NOT RUN. This is just the structure. The code needs definite definition to run. 
    