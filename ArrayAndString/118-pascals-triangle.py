# Problem: 118. Pascal's Triangle
# Link: https://leetcode.com/problems/pascals-triangle/

# Time Complexity: O(n ^ 2)
# Space Complexity: O(n ^ 2)
# (the result list stores all rows, each row is a list of integers)
# (the total numbers of elements stored in the result list is n/(n + 1)/2 where n = numRows)


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        count = 3

        if numRows >= 1:
            result.append([1])
        if numRows >= 2:
            result.append([1, 1])

        while count <= numRows:
            temp_list = []
            temp_list.append(1)
            length = len(result)

            for i in range(1, len(result[length - 1])):
                sum_above = result[length - 1][i - 1] + result[length - 1][i]
                temp_list.append(sum_above)

            temp_list.append(1)
            result.append(temp_list)
            count += 1

        return result
