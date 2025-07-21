# Problem: 557. Reverse Words in a String III
# Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/

# Time Complexity: O(n)
# Space Complexity: O(n)
# (n = the length of the input string)

# solution using join instead of string concatenation


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()  # O(n) time complexity for the split built-in function
        word_count = len(words)
        result_string = []

        for i in range(word_count):  # O(n)
            result_string.append(words[i][::-1])
            # O(k) for reversing a word, where k = the length of the word

        return " ".join(result_string)  # O(n)


'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()  # O(n)
        word_count = len(words)
        result_string = ""

        for i in range(word_count):  
            result_string += words[i][::-1]
            if i != word_count - 1:
                result_string += " "

        return result_string
'''
