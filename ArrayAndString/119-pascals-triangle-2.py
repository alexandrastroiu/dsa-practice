# Problem: 119. Pascal's Triangle II
# Link: https://leetcode.com/problems/pascals-triangle-ii/


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]

        for i in range(rowIndex):
            row.append(1)
            for j in range(i, 0, -1):
                row[j] += row[j - 1]

        return row
