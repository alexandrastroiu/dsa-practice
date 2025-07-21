# Problem: 151. Reverse Words in a String
# Link: https://leetcode.com/problems/reverse-words-in-a-string/

# Time Complexity: O(n)
# Space Complexity: O(n)
# ( n = the number of characters in the string s)

# the solution using join instead of string concatenation


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reverse_str = []
        s = s.strip()  # O(n) for the built-in method strip
        index = length = len(s)

        for i in range(length - 1, -1, -1):  # 0(n)
            if s[i] == " " and s[i + 1] != " ":
                reverse_str.append(s[i + 1 : index])
                # O(k) (k = the length of the sublist)
            if s[i] == " ":
                index = i

        reverse_str.append(s[0:index])

        return " ".join(reverse_str)  # O(n)


# the solution using concatenation

'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reverse_str = ""
        s = s.strip()  # O(n) for the built-in method strip
        index = length = len(s)

        for i in range(length - 1, -1, -1):  # O(n)
            if s[i] == " " and s[i + 1] != " ":
                reverse_str += s[i + 1 : index]
                reverse_str += " "
            if s[i] == " ":
                index = i

        reverse_str += s[0:index]

        return reverse_str
        '''

# Alternative solution using built-in functions only
# return ' '.join(s.split()[::-1])
