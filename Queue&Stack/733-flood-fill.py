# Problem: 733. Flood Fill
# Link: https://leetcode.com/problems/flood-fill/


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        # number of rows
        rows = len(image)
        # number of columns
        cols = len(image[0])
        # the original color
        original_color = image[sr][sc]
        # directions for neighboring pixels
        directions = set(((0, -1), (0, 1), (1, 0), (-1, 0)))

        # helper function used to fill the original matrix
        def fill(row, col):
            # if the pixel if already the target color or not the original color, return
            if image[row][col] == color or image[row][col] != original_color:
                return

            # if the pixel is the original color, modify it and check neighboring pixels
            if image[row][col] == original_color:
                image[row][col] = color

                for x, y in directions:
                    new_row = row + x
                    new_col = col + y
                    # check for valid row and column
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        # repeat the process by calling the function recursively
                        fill(new_row, new_col)

        # call the helper function
        # the process starts at image[sr][sc]
        fill(sr, sc)
        # return the modified matrix
        return image
