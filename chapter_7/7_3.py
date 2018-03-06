"""
Check for cyclicity
Given a linked list, is it cyclical or does it end?

Interesting problem.  So, if a list is cyclical, eventually the values
will repeat.  Now, we can assume that if a list repeats itself once, 
then we will see nodes that already existed.

Given a list and 2 iterators, first we have one fast iterator and one
slow iterator.  Eventually the, the fast iterator will == the slow,
or it will be null.
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

def is_cyclical(head):
    slow = head
    fast = head.next
    if fast == None:
        return False
    while fast.next:
        if slow == fast:
            return True
        fast = fast.next
    return False

if __name__ == "__main__":
    node_c = ListNode(5)
    node_b = ListNode(1, node_c)
    node_a = ListNode(0, node_b)
    node_d = ListNode(4, node_a)
    node_c.next = node_d

    print(is_cyclical(node_d))
