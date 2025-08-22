# Problem: 380. Insert Delete GetRandom O(1)
# Link: https://leetcode.com/problems/insert-delete-getrandom-o1/

import random

# each function works in O(1) average time complexity


class RandomizedSet:

    # initializes the RandomizedSet object
    def __init__(self):
        # use a hashmap to map values to their index
        # in order to have O(1) time complexity for removing an element and for searching a value in the list
        self.index_hashmap = {}
        # adding an element to the list and accessing an element has O(1) time complexity for a list
        self.randomized_set = []

    def insert(self, val: int) -> bool:
        # only add if the value is not present in the set
        # look-up ina hashmap has O(1) time complexity
        if val not in self.index_hashmap:
            # map the value to the index
            self.index_hashmap[val] = len(self.randomized_set)
            # add the element to the list (O(1))
            self.randomized_set.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        # check if the value is in the set
        # look-up in a hashmap has O(1) time complexity
        if val in self.index_hashmap:
            # get the index of the element that will be removed
            removed_pos = self.index_hashmap[val]
            # swap the element that will be removed with the last element
            self.randomized_set[removed_pos] = self.randomized_set[-1]
            # update the index of the last element in the hashmap
            self.index_hashmap[self.randomized_set[-1]] = removed_pos
            # remove the element with the value val from the set
            # remove from the hashmap and remove from the list
            self.index_hashmap.pop(val)
            self.randomized_set.pop()
            return True
        return False

    def getRandom(self) -> int:
        # use the random module to return a random element from the list
        # random acces is O(1) on a list
        return random.choice(self.randomized_set)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# alternative solution: use only one data structure, a set
# however, the getRandom function will not work in O(1) time complexity

"""
import random

class RandomizedSet:

    def __init__(self):
        self.set = set()
        

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.set.add(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(list(self.set))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
"""
