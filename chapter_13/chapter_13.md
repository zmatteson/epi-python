- [Sorting](#sorting)
- [Tip & Tricks](#tip-tricks)
- [Sorting Libraries](#sorting-libraries)

Sorting
=======

* Quicksort is usually the best choice
* For short arrays, insertion sort is faster 
* Heaps can be used for k sorted arrays 
* If there are a small number of distinct keys, counting sort works well
* In-place sort is in place O(1)
* Stable sorts is where entries which are equal appear in their original order
  * Mergesort implemented carefully can be stable
  * ex (Kiwi, Spork, Banana, Steel sorted by first letter would return Banana, Kiwi, Spork, Steel - this is not guaranteed in an unstable sort)
* Most sorting routines are comparison based, but some (radix) use numerical attributes
* Time complexity of most good sorting algorithms O(n log n). Most library implementations use quicksort, which is in-place

Tip & Tricks
============

* Sorting problems come in two flavors (1) use sorting to make subsequent steps in an algorithm simpler, and (2) design a sorting routine.  For the former, it's fine to use a library sort function, possibly with a custom parameter.  For the latter, use a data structure like a BST, heap, or array indexed by values
* Certain problems become easier to understand, as well as solve, when the input is sorted. The most natural reason to sort is if the inputs have a <b>natural ordering</b>, and sorting can be used as a preprocessing step to speed up searching
* For specialized input, e.g., a very small range of values, or a small number of values, it's possible to sort in O(n) time rather than O(n log n) time
* It's often the case that sorting can be implemented in less space than required by a brute-force approach
* Sometimes it's not obvious what to sort on, e.g., should a collection of intervals be sorted on their start or end points?

Sorting Libraries
=================

* To sort a list in place, use `sort()`, to sort an iterable, use `sorted()`
* sort() implements a stable in-place sort for list objects. It returns None and takes two armguments (optional), key=None, and reverse=False
    * a = [1, 2, 4, 0, 10, 100], a.sort(key=lambda x: str(x)) maps the ints to strings and a becomes [0,1,10,100,2,4] according to lexographical ordering
    * If reverse=True, sort is taken in descending order
* sorted() takes and iterable and returns a new list in ascending order.  The old list is unchanged.  The optional arguments work the same