Dynamic Programming
===================

* DP is a general technique for solving optimization, search, and counting problems that can be decomposed into subproblems. You should consider using DP whenever you jave to make choices to arrive at the soultion, sepcifically when the solution relates to subproblems
* Consider using DP when you have to make CHOICES to arrive at the solution
* In addition to optimization problems, DP is also applicable to counting and decision problems--any problem where you can express a solution recursively in terms of the same computation on smaller instances
* Although conceptually DP involves recursion, often for efficieny the cache is built "bottom-up", i.e., iteravely
* When DP is implemented recursively, the cache is typically a dynamic data structure such as a hash table or a BST; when it is implemented iteratively the cache is usually a one or multi dimensional array
* to save space, cache space may be recycled once it is known a set of entries won't be looked up again
* Sometimes recursion may out-perform a bottom-up DP solution, e.g., when the solution is found early or subproblems can be pruned through bounding
* A common mistake in DP is trying to think of the recursive case by splitting the problem into two equal halves, a la quicksort. However, in most cases, this is not sufficient
* DP is based on combining solutions to subproblems to yield a solution to the original problem. However, for some problems DP will not work.