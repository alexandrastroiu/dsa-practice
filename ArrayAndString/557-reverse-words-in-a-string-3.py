# Problem: 557. Reverse Words in a String III
# Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        word_count = len(words)
        result_string = ""

        for i in range(word_count):
            result_string += words[i][::-1]
            if i != word_count - 1:
                result_string += " "

        return result_string
