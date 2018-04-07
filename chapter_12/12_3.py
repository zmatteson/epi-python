"""
Implement an isbn cache

Rules for ISBN:

9 digits, 10th being a checksum mod 11, with 10 represented as X

Create a cache for looking up prices of books identified by their ISBN

You implement lookup, insert, and remove methods.  Use the least recently used policy for cache eviction. If an ISBN is already present, insert should not change the price, but it should update that entry to be the most recently used entry.  lookup should also update that entry to be the most recently used entry

Basic idea: implement a cache class with a hash table with a tuple
Store the keys in a queue?

Let’s say that 10 is the size of the cache.  
We could use 2 hash tables. One to store the ordering, one to store the times.  But how do we quickly bump down the other entries?

One idea: use a linked list
Use a priority queue?
Another idea: use an array? 

Think of more things… 
"""
import collections

class IsbnCache:
    def __init__(self, capacity = 100):
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def lookup(self, isbn):
        if isbn in self.cache:
            price = self.cache.pop(isbn)
            self.cache[isbn] = price
            return price
        else:
            return None
    
    def insert(self, isbn, price):
        if not self.lookup(isbn):
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
            self.cache[isbn] = price
    
    def delete(self, isbn):
        if isbn in self.cache:
            self.cache.pop(isbn)

if __name__ == '__main__':
    cache = IsbnCache(2)
    cache.insert('A', 1)
    print(cache.lookup('A'))
    cache.insert('A', 2)
    print(cache.lookup('A'))
    cache.insert('B', 2)
    print(cache.lookup('B'))
    cache.insert('C', 3)
    print(cache.lookup('A'))
    cache.delete('B')
    print(cache.lookup('B'))