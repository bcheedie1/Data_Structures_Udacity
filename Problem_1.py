# Write your code here :-)
from collections import deque


class LRU_Cache(object):
    def __init__(self, capacity):
        self.our_cache = {}
        self.cache_order = deque()
        self.capacity = 5

    def get(self, key):
        if key in self.our_cache:
            self.cache_order.remove(key)
            self.cache_order.appendleft(key)
            return self.our_cache[key]
        else:
            return -1

    def put(self, key, value):
        if key in self.our_cache:
            self.cache_order.remove(key)
        elif len(self.our_cache) >= self.capacity:
            # Remove the least recently used element
            lru_key = self.cache_order.pop()
            self.our_cache.pop(lru_key)
        self.our_cache[key] = value
        self.cache_order.appendleft(key)


our_cache = LRU_Cache(5)
our_cache.put(1, 1)
our_cache.put(2, 2)
our_cache.put(3, 3)
our_cache.put(4, 4)
our_cache.put(5, 5)

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1

our_cache.put(6, 6)  # Adds new element, 6, replacing the least used element, 3

print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

our_cache.put(525600, 'Q')  #replaces the LRU 4
our_cache.put('A', 10)      #replaces the LRU 5
our_cache.put(-5, 'string') #replaces the LRU 1

print(our_cache.get(-5))        # returns string      
print(our_cache.get(525600))    # returns Q
print(our_cache.get(0))         # not in cache, returns -1
print(our_cache.get('A'))       # returns 10
print(our_cache.get(1))         # not in cache because it was replaced, returns -1

