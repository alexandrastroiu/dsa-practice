# Problem: 454. 4Sum II
# Link: https://leetcode.com/problems/4sum-ii/

# brute-force solution: O(n^4)
# optimized solution: O(n^2)


class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        hashmap = {}
        zeros = 0

        for i in nums1:
            for j in nums2:
                current_sum = i + j
                if current_sum in hashmap:
                    hashmap[current_sum] += 1
                else:
                    hashmap[current_sum] = 1

        for i in nums3:
            for j in nums4:
                complement_sum = i + j
                if -complement_sum in hashmap:
                    zeros += hashmap[-complement_sum]

        return zeros
