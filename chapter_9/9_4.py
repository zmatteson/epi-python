"""
Compute the lowest common ancestor.  Assume each node has a parent pointer

         A
     B      C

Compute path to root for each node.  Compare each path from the shortest level. 

"""

class TreeNode:
    def __init__(self, id = None, right = None, left = None, parent = None):
        self.id = id
        self.right = right
        self.left = left
        self.parent = parent

def build_tree():
    root = TreeNode(1,None,None,None)
    left = TreeNode(2,None,None,root)
    right = TreeNode(3,None,None,root)
    l1 = TreeNode(4,None,None,left)
    left.left = l1
    l2 = TreeNode(5,None,None,l1)
    l1.left = l2
    root.left = left
    root.right = right
    return l1, l2

def get_path(node_a):
    path = []
    temp = node_a.parent
    while temp:
        path.append(temp.id)
        temp = temp.parent
    return path

def get_lcm(node_a, node_b):
    path_a = get_path(node_a)
    path_b = get_path(node_b)
    if len(path_a) >= len(path_b):
        return get_lcm_from_path(path_a, path_b)
    else:
        return get_lcm_from_path(path_b, path_a)

def get_lcm_from_path(long_path, short_path):
    diff = len(long_path) - len(short_path)
    for i in range(len(short_path)):
        if short_path[i] == long_path[i+diff]:
            return short_path[i]
    raise ValueError('The nodes are not in the same tree')

if __name__ == "__main__":
    node_a, node_b = build_tree()
    print(get_lcm(node_a, node_b))