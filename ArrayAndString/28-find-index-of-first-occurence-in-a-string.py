# Problem: 28. Find the Index of the First Occurrence in a String
# Link:https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # using the find() method
        return haystack.find(needle)
