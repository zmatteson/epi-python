* Use a heap when all you care about is the largest or smallest elements, and you do not need to support fast lookup, delete, or search operations for arbitrary elements
* A heap is a good choice when you need to compute the k largest or k smallest elements in a collection.  For the former, use a min-heap, for the latter, use a max-heap

Heaps in Python
===============

* Heap functionality is provided by hte heapq.heapify(L) which transforms L into a heap in-place
* heapq.nlargest(k, L) (heapq.nsmallest(k,L)) returns the k-largest (smallest) elements in L
* heapq.heappush(h, e) pushes a new element on the heap
* heapq.heappop(h) pops the smallest element from the heap
* heapq.heappushpop(h,a) pushes a on the heap and then pops and returns the smallest element
* e = h[0] returns the smallest element without popping it
* heapq only provides MIN-HEAP functionality.  If you need to build a max-heap on integers or floats, inset their negative to get the effect of a max-heap using heapq.  For objects, implement __lt()__ appropriately 