"""
Given a binary tree, return an array consisting of the keys at the same level
Keys should appear left to right

1 -> 2 -> 5
       -> 6
  -> 4 -> 7

returns [[1],[2,4],[5,6,7]]
Make 2 arrays, one to hold the levels
Add the root to the level, and it's children to the next level

""" 
class TreeNode():
    def __init__(self,left,right,key):
        self.key = key
        self.left = left
        self.right = right

    
def get_num_child(root):
    ans = 0
    if root.left:
        ans += 1
    if root.right:
        ans += 1
    return ans
def make_tree(root):
    if not root:
        return []
    tree = []
    ans = [[]]
    level = 0
    nodes_per_level = 1
    tree.append(root)
    while(tree):
        temp_count = 0
        for _ in range(nodes_per_level):
            temp = tree.pop(0)
            temp_count += get_num_child(temp)
            ans[level].append(temp.key)
            if (temp.left):
                tree.append(temp.left)
            if (temp.right):
                tree.append(temp.right)
        level += 1
        ans.append([])
        nodes_per_level = temp_count
    return ans[:-1]

if __name__ == "__main__":
    node_E = TreeNode(None,None,5)
    node_D = TreeNode(None,None, 4)
    node_C = TreeNode(node_D,node_E,3)
    node_B = TreeNode(None,None,2)
    node_A = TreeNode(node_B,node_C,1)
    print(make_tree(node_A))