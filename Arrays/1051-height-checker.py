# Problem: 1051. Height Checker
# Link: https://leetcode.com/problems/height-checker/


# Time Complexity: O(nlog(n))
# Space Complexity: O(n)


class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)  # O(nlog(n))
        count = 0

        for i in range(len(heights)):  # O(n)
            if expected[i] != heights[i]:
                count += 1

        return count
