# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

# Example 1:

# Input:
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output:
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4



class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    # Use a doubly-linked list to enable O(1) "get" and "put" operations.
    # Combine with a hashmap storing key:node to optimize lookup.

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key:node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # Helper functions to add/remove a node.
    def insert(self, node): # Adds a node to the list as the MRU.
        prev = self.right.prev
        prev.next = node
        node.next = self.right
        self.right.prev = node
        node.prev = prev

    def remove(self, node): # Removes a node.
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev


    def get(self, key: int) -> int:
        # Retrieve the node if it exists. Make this node the MRU.
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # Add a new key:value pair. If that key has already been stored, need to add then remove the node and modify the cache.

        if key in self.cache:
            self.remove(self.cache[key])

        newNode = Node(key, value)
        self.insert(newNode)
        self.cache[key] = newNode

        # Now, if capacity is exceeded -> remove LRU (the node immediately to the right of self.left).
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Time Complexity: O(1) -> Lookup in hashmap is O(1). Insert/Remove is also O(1).
# Space Complexity: O(capacity) -> Store nodes in hashmap and linked list up to capacity.


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



# 2nd Solution:

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None

class LRUCache:
    # Use a doubly-linked list to enable O(1) "get" and "put" operations.

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # stores key:node
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # Helper functions to insert/remove nodes.
    def insert(self, node):
        # Insert node as MRU.
        prev = self.right.prev
        prev.next = node
        node.next = self.right
        self.right.prev = node
        node.prev = prev

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev


    def get(self, key: int) -> int: # Looks for a node. If exists, make it the MRU AND return the value. If not found, return -1.
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1


    def put(self, key: int, value: int) -> None: # Inserts a node as the MRU. If it exists, remove it and THEN insert as the MRU. Must update self.cache, as well.
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity: # If capacity is exceeded, remove LRU.
            lru = self.left.next
            self.remove(self.cache[lru.key])
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Time Complexity:
#   - init: O(1)
#   - get: O(1) -> O(1) for lookup and insertion/removal of a node.
#   - put: O(1) -> O(1) for lookup and insertion/removal of a node.

# Space Complexity: O(capacity) -> Cache will store a key/node pair up to self.capacity.