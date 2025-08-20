# Problem: 599. Minimum Index Sum of Two Lists
# Link: https://leetcode.com/problems/minimum-index-sum-of-two-lists/


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # convert the lists to sets
        set1 = set(list1)
        set2 = set(list2)
        hashmap = {}
        result = []
        minimum_sum = 2e3

        # parse the words in set1
        for word in set1:
            # if the word is also found in set2 (O(1) for look-up in a set)
            if word in set2:
                # add the pair to the hashmap (the value is the sum of indexes)
                hashmap[word] = list1.index(word) + list2.index(word)
                # update the minimum value
                minimum_sum = min(minimum_sum, hashmap[word])

        # parse the pairs in the hashmap
        for key in hashmap:
            # add all words that have the minimum sum of indexes to the result list
            if hashmap[key] == minimum_sum:
                result.append(key)

        return result
