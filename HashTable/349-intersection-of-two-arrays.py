# Problem: 349. Intersection of Two Arrays
# Link: https://leetcode.com/problems/intersection-of-two-arrays/


# one-liner solution that uses type conversion and the '&' built-in intersection operator on sets
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


# alternative solution
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # convert the lists to sets to remove duplicate values
        nums1 = set(nums1)
        nums2 = set(nums2)
        # the list taht will be returned
        result = []

        # parse the set with less elements
        if len(nums1) < len(nums2):
            for num in nums1:
                # for each element check if the element is found in the other set
                # if the element is part of the 'intersection', add it to the result list
                # look-up in a set is O(1)
                if num in nums2:
                    result.append(num)
        else:
            for num in nums2:
                if num in nums1:
                    result.append(num)

        return result
"""
