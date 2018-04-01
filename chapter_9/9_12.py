"""
Reconstruct a binary tree given

inorder traversal sequence 
and 
preorder traversal sequence

ex. inorder : F,B,A,E,H,C,D,I,G
    preorder: H,B,F,E,A,C,D,G,I

"""
class TreeNode:
    def __init__(self, left = None, right = None, key = None):
        self.left = left
        self.right = right
        self.key = key

def print_preorder(root):
    if root:
        print(root.key,end='')
        print_preorder(root.left)
        print_preorder(root.right)

def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.key,end='')
        print_inorder(root.right)

def insert(node, root, tree_map):
    if tree_map[node.key] < tree_map[root.key]:
        if not root.left:
            root.left = node
        else:
            insert(node, root.left, tree_map)
    if tree_map[node.key] > tree_map[root.key]:
        if not root.right:
            root.right = node
        else:
            insert(node, root.right, tree_map)

def reconstruct_tree(inorder, preorder):
    tree_map = {}
    for i, key in enumerate(inorder):
        tree_map[key] = i
    root = TreeNode(None, None,preorder[0])
    
    for i in range(1, len(preorder)):
        node = TreeNode(None, None,preorder[i])
        insert(node, root, tree_map)
    return root

#Time O(n log(n))
#Space O(n)

if __name__ == '__main__':
    inorder = ['F','B','A','E','H','C','D','I','G']
    preorder = ['H','B','F','E','A','C','D','G','I']
    root = reconstruct_tree(inorder,preorder)
    print_inorder(root)
    print()
    print_preorder(root)
    print()
    print(root.left.key, root.right.key)

