Hash tables
===========
- [Hash tables](#hash-tables)
- [Python hash table libraries](#python-hash-table-libraries)

Python hash table libraries
===========================
* set
  * Sets only contain keys
  * Set operations are s.add(x), s.remove(x), s.discard(), x in s, s <= t, s - t (elements in s that are not in t)
* dict
  * if a key is not present, can throw a KeyError  
* collections.defaultdict
  * if a key is not present, returns a default value (eg d = collections.defaultdict(list), d[k] would return []) 
* collections.Counter
  * can use 2 counters with math operations (b + a,a - b,a & b (intersection), a|b (union))
* To iterate over values, standard returns keys. values() returns values, key() returns keys, items() returns key value pairs
* Not every type is hashable - i.e. mutable containers
* Built in hash function can simplify implementation for a user defined class (implementing `__hash(self)__`)
* other dicts like OrderedDict exist that remember the last lookup