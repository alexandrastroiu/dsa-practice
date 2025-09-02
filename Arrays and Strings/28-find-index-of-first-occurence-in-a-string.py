# Problem: 28. Find the Index of the First Occurrence in a String
# Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

# Time Complexity: O(m * n) (the time complexity of the buil-in function find())
# (m = the length of the string in which the substring is searched, n = the length of the substring)
# Space Complexity: O(1)


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # using the find() method
        return haystack.find(needle)
