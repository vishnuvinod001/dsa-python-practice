# 236. Lowest Common Ancestor of a Binary Tree
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

def lowestCommonAncestor(self, root, p, q):
    
    if not root or root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    
    if left and right:
        return right

    return left if left else right


    """
    Here the nodes themselves can be their ancestors. So if you get p/q in the root itself we can return that.
    * Recursively go through the left and right to see if they return p or q.
    * In the case where both of them return something, we can return the current node as the LCA.
    * If only left or right has the answer, the info is passed to the parent of the current node and it becomes the LCA.
    
        5
      /   \
     6     2
          /
         7

p = 6
q = 7
    
    * At node 5, left becomes 6. 
    * At node 2, right becomes None but left is 7. => return 7
    * => at Node:5 left = 6, right = 7.
    * If left and right; return node => RETURNS 5 


    """