"""
Height balanced
Check if a tree is height balanced
A tree is not height balanced if any one of its subtrees has a height difference greater than 1

example:

              1
    2                  2
       3
          4

"""
class TreeNode:
    def __init__(self, left = None, right = None, key = None):
        self.left = left
        self.right = right
        self.key = key

def is_balanced(root):
    if root is None:
        return True
    return (abs(height(root.left) - height(root.right)) <= 1) and (is_balanced(root.left) and   
        is_balanced(root.right))

def height(root):
    if root == None:
        return 0
    return max(1+height(root.left), 1+height(root.right))

if __name__ == "__main__":
    nodeE = TreeNode(None,None, 4)
    nodeD = TreeNode(None,nodeE,3)
    left = TreeNode(None,nodeD,2)
    right = TreeNode(None,None,2)
    root = TreeNode(left, right, 1)
    print(is_balanced(root))

    left = TreeNode(None,None,2)
    right = TreeNode(None,None,2)
    root = TreeNode(left, right, 1)
    print(is_balanced(root))


    left = TreeNode(None,None,2)
    root = TreeNode(left, None, 1)
    print(is_balanced(root))