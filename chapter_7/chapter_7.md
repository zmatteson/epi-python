* List problems often have a simple brute-force solution that uses O(n) space, but a subtler solution that uses the existing list nodes to reduce space complexity to O(1)
* Very often, a problem on lists is conceptually simple, and if more about cleanly coding what's specified, rather than designing an algorithm
* Consider having a dummy head (sometimes referred to as a sentinel) to avoid having to check for empty lists. This simplifies code, and makes bugs less likely
* It's easy to forget to update next(and previous for double linked list) for the head and tail
* Algorithms operating on singly linked lists often benefit from using two iterators, one ahead of the othher, or one advancing quicker than the other