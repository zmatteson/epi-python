* Array problems often have simply brute force solutions that use O(n) space, but there are subtle soultions that use the array itself to reduce space complexity to O(1)

* Filling an array from the front is slow, so see if it's possible to write values from the back

* Instead of deleting an entry (which requires shifting), consider overwriting

* When dealing with integers encoded by an array consider processing the digits from the back of the array. Alternatively, reverse the array so the least-significant digit is the first entry
* Be comfortable with writing code that operates on subarrays
* It's incredibly easy to make off-by-1 errors when operatoing on arrays -- reading past the last element of an array is a common error which has catastrophic consequences
* Don't worry about perserving the integrity of the array (sortedness, keeping equal entries together, etc ) until it's time to return
* An array can serve as a good data structure when you know the distribution of the elements in advance. For example, a Boolean array of length W is a good choice for representing a subset of {0,1,...,W-1} (When using a Boolean array to represent a subset of {1,2,3 ... n} allocate an array of size n + 1 to simplify indexing)
* When operating on 2D arrays, use parallel logic for rows and colums
* Sometimes it's easier to simulate the specification, than to analytically solve the result. For example, rather than writing a formula for the i-th entry in the spiral order for an nxn matrix, just compute the output from the beginning