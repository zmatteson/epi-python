"""
Test if a tree is symmetric

1 -> 2
  -> 2
"""
class TreeNode:
    def __init__(self, left = None, right = None, key = None):
        self.left = left
        self.right = right
        self.key = key

def is_symmetric_rec(root):
    return check_symmetric(root.left, root.right)

def check_symmetric(left, right):
    if not left and not right:
        return True
    else:
        return (left.key == right.key and check_symmetric(left.left, right.right)
            and check_symmetric(left.right, right.left))

def is_symmetric(root):
    left, right = [], []
    left = traverse_left(root.left, left)
    right = traverse_right(root.right, right)
    print(left, right)
    while left and right:
        if left.pop() is not right.pop():
            return False
    if left or right:
        return False
    return True

def traverse_left(root, stack):
    if not root:
        return stack
    stack.append(root.key)
    if root.left:
        traverse_left(root.left, stack)
    else:
        stack.append(None)
    if root.right:
        traverse_left(root.right, stack)
    else:
        stack.append(None)
    return stack

def traverse_right(root, stack):
    if not root:
        return stack
    stack.append(root.key)
    if root.right:
        traverse_right(root.right, stack)
    else:
        stack.append(None)
    if root.left:
        traverse_right(root.left, stack)
    else:
        stack.append(None)
    return stack

if __name__ == "__main__":
    left = TreeNode(None,None,2)
    right = TreeNode(None,None,2)
    root = TreeNode(left, right, 1)
    print(is_symmetric_rec(root))
