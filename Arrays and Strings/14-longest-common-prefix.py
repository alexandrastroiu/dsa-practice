# Problem: 14. Longest Common Prefix
# Link: https://leetcode.com/problems/longest-common-prefix/

# Time Complexity: O(m * n) (m = the length of the shortest word in strs, n = the number of words in strs)
# Space Complexity: O(k)    (k = the length of the longest common prefix)

# the solution using join instead of string concatenation is more efficient and clean
# using the join built-in function avoid repeated copying of strings


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest_prefix = []
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
                longest_prefix.append(word[i])

            i += 1

        return "".join(longest_prefix)  # O(m)


# the solution using concatenation

'''
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
'''
