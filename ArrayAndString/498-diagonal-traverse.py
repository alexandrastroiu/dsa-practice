# Problem: 498. Diagonal Traverse
# Link: https://leetcode.com/problems/diagonal-traverse/


class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        rows = len(mat)
        cols = len(mat[0])
        result = []
        val = rows + cols - 1

        for k in range(val):
            if k < cols:
                if k % 2 == 0:
                    for i in range(k, -1, -1):
                        if 0 <= k - i < cols and 0 <= i < rows:
                            result.append(mat[i][k - i])
                else:
                    for i in range(k + 1):
                        if 0 <= k - i < cols and 0 <= i < rows:
                            result.append(mat[i][k - i])
            else:
                if k % 2 == 0:
                    for i in range(min(rows - 1, k), max(0, k - cols + 1) - 1, -1):
                        if 0 <= k - i < cols:
                            result.append(mat[i][k - i])
                else:
                    for i in range(max(0, k - cols + 1), min(rows, k + 1), 1):
                        if 0 <= k - i < cols:
                            result.append(mat[i][k - i])

        return result
