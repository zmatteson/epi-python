"""
Find LCA in BST
"""
import collections

class TreeNode:
    def __init__(self, left = None, right = None, key = None):
        self.left = left
        self.right = right
        self.key = key


def find_bst_lca(root, a, b):
    return find_lca(root, b, a)

def find_lca(root, b, a):
    path_b, path_a = root, root
    while path_b and path_a:
        root = path_a
        if path_b.key > b.key:
            path_b = path_b.left
        else:
            path_b = path_b.right

        if path_a.key > a.key:
            path_a = path_a.left
        else:
            path_a = path_a.right
        
        if path_b != path_a or (path_b == b) or (path_a == a):
            return root.key
    return None
        

def find_lca_in_path(a, b):
    print(a,b)
    count = collections.Counter(a)
    for key in b:
        if key in count:
            if (a[-1] < key < b[-1]) or (a[-1] > key > b[-1]):
                return key     
    return None
 
def get_path(root, node):
    path = []
    while root:
        path.append(root)
        if root.key > node.key:
            root = root.left
        elif root.key == node.key:
            break
        else:
            root = root.right
    return path

if __name__ == '__main__':
    nodeE = TreeNode(None,None, 9)
    nodeD = TreeNode(None,nodeE,7)
    left = TreeNode(None,nodeD,5)
    right = TreeNode(None,None,15)
    root = TreeNode(left, right, 10)
    print(find_bst_lca(root, nodeE, nodeD))