Binary Search
=============
* Binary search is an effective tool. It is applicable to more than just searhcing in sorted arrays (e.g. it can be used to search an interval of real numbers or integers).
* If your solution uses sorting, and the computation performed after sorting is faster than sorting, look for solutions that do not perform a complete sort.
* Consider time/space tradeoffs, such as making multiple passes through the data

Searching libraries
===================

* The bisect module provides binary search functions for sorted lists.  Specifically, assuming a is a sorted list:
* * To find the first element that is not less than a targeted value, use bisect.bisect_left(a,x).  This call returns the index of the first entry that is greater than or eaqual to the targeted value.  If all elements in the list are less than x, the returned value is len(a)
* * To find the first element that is greater than a targeted value, use bisect.bisect_right(a,x) .  This call returns the index of the first entry that is greater than the targeted value.  If all elements in the list are less than or equal to x, the returned value is len(a)
* Use the above functions in an interview if possible