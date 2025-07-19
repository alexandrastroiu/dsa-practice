# Problem: 151. Reverse Words in a String
# Link: https://leetcode.com/problems/reverse-words-in-a-string/


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reverse_str = ""
        s = s.strip()
        index = length = len(s)

        for i in range(length - 1, -1, -1):
            if s[i] == " " and s[i + 1] != " ":
                reverse_str += s[i + 1 : index]
                reverse_str += " "
            if s[i] == " ":
                index = i

        reverse_str += s[0:index]

        return reverse_str

        # Alternative solution using built-in functions only
        # return ' '.join(s.split()[::-1])
