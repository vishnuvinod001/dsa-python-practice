import sys
from utils import parse_input
from build_tree import build_tree
from traversals import (
    inOrd, preOrd, postOrd
)

values = parse_input(sys.argv[1])
root = build_tree(values)

print("Preorder: ", preOrd(root))
print("Inorder: ", inOrd(root))
print("Postorder: ", postOrd(root))