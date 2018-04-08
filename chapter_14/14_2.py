class TreeNode:
    def __init__(self, left = None, right = None, key = None):
        self.left = left
        self.right = right
        self.key = key


def find_first_key_gt(root, x):
    return find_first_key_gt_util(root, x, float('-inf'))


def find_first_key_gt_util(root, key, parent):
    if root:
        print(root.key, key, parent)
        if key < root.key:
            ans = find_first_key_gt_util(root.left, key, root.key)
        if parent <= key < root.key:
            ans = min(root.key, ans)
        elif not root.left and key < root.key:
            ans = min(root.key, ans)
        if key >= root.key:
            ans = find_first_key_gt_util(root.right, key, root.key)
        return ans
    else:
        return float('inf')   

if __name__ == '__main__':
    nodeE = TreeNode(None,None, 9)
    nodeD = TreeNode(None,nodeE,7)
    left = TreeNode(None,nodeD,5)
    right = TreeNode(None,None,15)
    root = TreeNode(left, right, 10)
    print(find_first_key_gt(root, 0))