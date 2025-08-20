# Problem: 219. Contains Duplicate II
# Link: https://leetcode.com/problems/contains-duplicate-ii/


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # initialize the hashmap
        hashmap = {}

        # parse the input list
        for index, num in enumerate(nums):
            # if the current element is a key in the hash map
            if num in hashmap:
                # calculate the current difference
                difference = abs(index - hashmap[num])
                # check the condition
                if difference <= k:
                    return True
            # always keep the last index of the occurence as the value in the pair
            hashmap[num] = index

        # there are no two distinct indices that meet the condition
        return False
