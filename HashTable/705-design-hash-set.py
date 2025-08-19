# Problem: 705. Design HashSet
# Link: https://leetcode.com/problems/design-hashset/


class MyHashSet:

    def __init__(self, size=1000):
        # the size of the hash set
        self.size = size
        # initialize the list that contains the buckets, each bucket is a list
        self.set = [[] for _ in range(size)]

    # the hash function used to generate the hash code
    def hash_function(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        # determine what bucket the element belongs to in the hash set
        index = self.hash_function(key)
        bucket = self.set[index]
        # add the element
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        index = self.hash_function(key)
        bucket = self.set[index]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        index = self.hash_function(key)
        bucket = self.set[index]
        return key in bucket


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
