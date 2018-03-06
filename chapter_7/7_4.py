"""
Find if there is a common value
Two linked lists:
A couple different approaches:

1) search each list for each node (n^2)
2) Use a hash table (O(m+k) + O(n) space)
3) Find the tails of both lists

"""

def is_overlapping(L1, L2):
    iterator1, iterator2 = L1, L2
    while iterator1.next:
        iterator1 = iterator1.next
    while iterator2.next:
        iterator2 = iterator2.next
    if iterator1 == iterator2:
        return True
    else:
        return False

class ListNode:
    def __init__(self, data=0,next_node=None):
        self.data = data
        self.next = next_node
def print_list(node):
    while node:
        print(node.data, " -> ", end='')
        node = node.next
    print()

if __name__ == "__main__":
    node_c = ListNode(5)
    node_b = ListNode(1, node_c)
    node_a = ListNode(0, node_b)
    node_d = ListNode(4, node_a)

    node_e = ListNode(1)

    print(is_overlapping(node_d, node_e))

