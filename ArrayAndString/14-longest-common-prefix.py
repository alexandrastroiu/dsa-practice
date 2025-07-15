# Problem: 14. Longest Common Prefix
# Link: https://leetcode.com/problems/longest-common-prefix/


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest_prefix = ""
        words = len(strs)
        minimum_length = 200

        for word in strs:
            if len(word) < minimum_length:
                minimum_length = len(word)

        is_common_character = True
        i = 0

        while i < minimum_length:
            for word in strs:
                if word[i] != strs[0][i]:
                    is_common_character = False

            if is_common_character:
                longest_prefix += word[i]

            i += 1

        return longest_prefix
