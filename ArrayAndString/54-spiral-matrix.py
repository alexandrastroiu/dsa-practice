# Problem: 54. Spiral Matrix
# Link: https://leetcode.com/problems/spiral-matrix/


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        cols = len(matrix[rows - 1])
        minimum = min(rows, cols)
        spiral_order = []

        # traversals = total number of traversals done in spiral order
        if minimum % 2 == 0:
            traversals = minimum // 2
        else:
            traversals = (minimum + 1) // 2

        for k in range(traversals):
            for j in range(k, cols - k):
                spiral_order.append(matrix[k][j])

            for i in range(k + 1, rows - k):
                spiral_order.append(matrix[i][cols - 1 - k])

            if rows - 1 - k != k:
                for j in range(cols - 2 - k, k - 1, -1):
                    spiral_order.append(matrix[rows - 1 - k][j])

            if cols - 1 - k != k:
                for i in range(rows - 2 - k, k, -1):
                    spiral_order.append(matrix[i][k])

        return spiral_order
