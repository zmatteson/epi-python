- [Recursion](#recursion)
- [Top tips](#top-tips)

Recursion
=========
* Approach to problem solving wherre the solution depends partially on solutions to smaller instances of related problems
* Searching, enumeration, divide-and-conquer, and decomposing a problem are all scenarious where recursion could be useful
* A recursive function involves base cases and calls to the same function with different arguments
* Merge sort and quick sort are classical examples of divide-and-conquer
* D&C is not synonymous with recursion
* Sometimes recursive problems are implemented using iteration instead of recursion

Top tips
========
* Recursion is especially suitable when the input expressed using recursive rules such as a computer grammar
* Recursion is a good choice for search, enumeration, and divide-and-conquer
* Use recursion as alternative to deeply nested iteration loops. For example, recursion is much better when you have an undefined number of levels
* If you are asked to remove recursion from a program, consider mimicking call stack with the stack data structure
* Recursion can be easily removed from a tail-recursive program while using a while-loop - no stack is needed
* If a recursive funxtion may end up being called with the same arguments more than once, cache the results (this is the idea behind DP)
