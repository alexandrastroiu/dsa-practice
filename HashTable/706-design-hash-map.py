# Problem: 706. Design HashMap
# Link: https://leetcode.com/problems/design-hashmap/


class MyHashMap:

    def __init__(self, size=1000):
        # the size of the hash map
        self.size = size
        # the list that contains the buckets, each bucket is a list in order to handle collisions
        self.table = [[] for _ in range(size)]

    # teh hash function used to generate hash codes
    def hash_function(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        # generate the hash code (index) by hashing the key value
        index = self.hash_function(key)
        # place the element in the corresponding bucket
        bucket = self.table[index]
        # check if the pair is already in the bucket or not
        for i, entry in enumerate(bucket):
            entry_key, entry_value = entry
            if entry_key == key:
                # update the value and return
                bucket[i] = (key, value)
                return
        # add the pair to the bucket
        bucket.append((key, value))

    def get(self, key: int) -> int:
        index = self.hash_function(key)
        bucket = self.table[index]
        for entry in bucket:
            entry_key, entry_value = entry
            # if the key is in the bucket, return the value
            if entry_key == key:
                return entry_value
        return -1

    def remove(self, key: int) -> None:
        index = self.hash_function(key)
        bucket = self.table[index]
        for entry_index, entry in enumerate(bucket):
            entry_key, entry_value = entry
            if entry_key == key:
                # remove the pair from the bucket
                bucket.pop(entry_index)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
