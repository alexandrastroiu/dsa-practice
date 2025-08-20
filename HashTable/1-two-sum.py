# Problem: 1. Two Sum
# Link: https://leetcode.com/problems/two-sum/

# brute-force : try all pairs O(n^2) time
# optimized: sort array, parse array and search for complement using binary search => O(nlogn) time
# optimized (with additional space): use a hashmap =>O(n) time , O(n) space (most common, most efficient solution)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initialize a hashmap
        # map distinct element values to their indexes
        hashmap = {}

        # parse the given list
        for index, num in enumerate(nums):
            # search for the 'pair' number
            pair_num = target - num

            # if the 'pair' number was encountered (is a key in the hashmap), return the result
            if pair_num in hashmap:
                hashmap[pair_num].append(index)
                return hashmap[pair_num]

            # map the index to its value
            if num in hashmap:
                hashmap[num].append(index)

            else:
                hashmap[num] = [index]
