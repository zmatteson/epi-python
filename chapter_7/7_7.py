"""
Remove kth element from the end of the list
You cannot record the length of the list
Use 2 iterators: one moving K steps, one normal
When Fast reaches tail, remove K
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

def remove_kth_node_from_end(L, k):
    dummy_head = slow = ListNode(0, L)
    fast = L
    while fast:
        for _ in range(k):
            fast = fast.next
        if fast == None:
            slow.next = slow.next.next
        else:
            for _ in range(k):
                slow = slow.next
    return dummy_head.next

if __name__ == "__main__":
    node_c = ListNode(5)
    node_b = ListNode(1, node_c)
    node_a = ListNode(0, node_b)
    node_d = ListNode(4, node_a)

    print_list(node_d)
    print_list(remove_kth_node_from_end(node_d, 4))