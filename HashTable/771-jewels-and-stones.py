# Problem: 771. Jewels and Stones
# Link: https://leetcode.com/problems/jewels-and-stones/


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        # initialize a set
        jewels_set = set()

        # add all jewels to the set
        for jewel in jewels:
            jewels_set.add(jewel)

        # parse the stones input string
        for stone in stones:
            # look-up in a set is O(1)
            if stone in jewels_set:
                # count the stones that are also jewels
                count += 1

        return count
