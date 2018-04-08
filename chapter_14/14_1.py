"""
test if a tree satisfies the BST property

What is a BST?  
"""
class TreeNode:
    def __init__(self, left = None, right = None, key = None):
        self.left = left
        self.right = right
        self.key = key

def check_bst(root):
    max_num = float('inf')
    min_num = float('-inf')
    return check_bst_helper(root, max_num, min_num)

def check_bst_helper(root, max_num, min_num):
    if not root:
        return True
    elif root.key > max_num or root.key < min_num:
        print(root.key, max_num, min_num)
        return False
    return (check_bst_helper(root.left, root.key, min_num) and check_bst_helper(root.right, max_num, root.key))


if __name__ == '__main__':
    nodeE = TreeNode(None,None, 9)
    nodeD = TreeNode(None,nodeE,7)
    left = TreeNode(None,nodeD,5)
    right = TreeNode(None,None,15)
    root = TreeNode(left, right, 10)
    print(check_bst(root))

        #    10
        # 5      15
        #   7
        #     2