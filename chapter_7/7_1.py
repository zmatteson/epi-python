"""
Merge two sorted lists.  Consider two sorted lists. Write a program that 
takes two lists, assumed to be sorted, and returns their sorted merge
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

def merge_two_sorted_lists(L1, L2):
    dummy_head = tail = ListNode()
    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next
    tail.next = L1 or L2
    return dummy_head.next

if __name__ == "__main__":
    node_b = ListNode(1)
    node_a = ListNode(0,node_b)
    node_d = ListNode(4)
    node_c = ListNode(3, node_d)

    node_a = merge_two_sorted_lists(node_a, node_c)
    print_list(node_a)