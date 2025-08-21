# Problem: 3. Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Time Complexity: O(n)
# (n - the number of characters in the input string)
# Space Complexity: O(m) (worst case m = n)
# (m - the maximum number of unique characters in a window)

# sliding window approach


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # initialize two pointers
        # i - the start of the current window
        # j - pointer used to iterate over the string
        i = j = 0
        length = len(s)
        max_length = 0
        # initialize a set to keep track of unique characters in the current window
        characters = set()

        # handle edge case first
        if length <= 1:
            return length

        # iterate over the input string using the pointer j
        while j < length:
            # if a character repeats in the current window (substring)
            # keep making the current window smaller by shifting the left pointer until there are no repeating characters
            if s[j] in characters:
                while s[j] in characters:
                    characters.remove(s[i])
                    i += 1
            # add the current character in the set (the character is always unique in the current window)
            characters.add(s[j])
            # update the maximum length
            # j - i + 1 is the length of the current window
            max_length = max(max_length, j - i + 1)
            j += 1

        # in the end, the algorithm will have compared the lengths of all substrings with unique characters
        # return the maximum length of a substring with unique characters
        return max_length
