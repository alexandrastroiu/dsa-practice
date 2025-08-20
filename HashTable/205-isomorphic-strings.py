# Problem: 205. Isomorphic Strings
# Link: https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        length_s = len(s)
        length_t = len(t)
        hashmap = {}

        # parse both input strings (it is guaranteed that the input strings have the same length)
        for i in range(length_s):
            char_s = s[i]
            char_t = t[i]

            # the strings are not isomorphic
            # one character corresponds to multiple characters from the second string
            if char_s in hashmap and hashmap[char_s] != char_t:
                return False

            # the strings are not isomorphic
            # a character in the second string is mapped to different characters from the first string
            if char_t in set(hashmap.values()) and char_s not in hashmap:
                return False

            # map characters from the first string to characters from the second string
            if char_s not in hashmap:
                hashmap[char_s] = char_t

        return True
