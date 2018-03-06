"""
Reverse a single sublist
Input: L, two integers, s and f, reverses the order of nodes from s to f

Traverse list to point s
Reverse sublist
Point s-1 to f, and s to f+1
"""
class ListNode:
    def __init__(self, data=0,next_node=None):
        self.data = data
        self.next = next_node
def print_list(node):
    while node:
        print(node.data, " -> ", end='')
        node = node.next
    print()

def reverse_sublist(head, s, f):
    dummy_head = sublist_head = ListNode(0,head)
    i = s - 1
    print(i)
    while i:
        sublist_head = sublist_head.next
        i = i - 1
    sublist_iter = sublist_head.next
    for _ in range (f - s):
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp

    return dummy_head.next
    
if __name__ == "__main__":
    node_c = ListNode(5)
    node_b = ListNode(1, node_c)
    node_a = ListNode(0, node_b)
    node_d = ListNode(4, node_a)

    print_list(node_d)
    print_list(reverse_sublist(node_d, 1, 4))
