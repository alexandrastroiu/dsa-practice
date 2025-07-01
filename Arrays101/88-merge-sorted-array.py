# Problem: 88. Merge Sorted Array
# Link: https://leetcode.com/problems/merge-sorted-array/


# Time Complexity: O(m + n)
# Space Complexity: O(m + n)


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        left = right = 0
        new_list = []

        while left < m and right < n:
            if nums1[left] <= nums2[right]:
                new_list.append(nums1[left])
                left += 1
            else:
                new_list.append(nums2[right])
                right += 1

        while left < m:
            new_list.append(nums1[left])
            left += 1

        while right < n:
            new_list.append(nums2[right])
            right += 1

        for i in range(m + n):
            nums1[i] = new_list[i]
