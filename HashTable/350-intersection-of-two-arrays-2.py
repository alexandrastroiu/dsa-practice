# Problem: 350. Intersection of Two Arrays II
# Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        hashmap = {}

        # parse the input list
        for num in nums1:
            # if the element is in both lists, but it not mapped yet
            # map the element to the common number of occurences in both lists
            if nums1.count(num) > 0 and nums2.count(num) > 0 and num not in hashmap:
                hashmap[num] = min(nums1.count(num), nums2.count(num))
                # add the element to the result list as many times as it appears in both input lists
                result.extend([num] * hashmap[num])

        return result
