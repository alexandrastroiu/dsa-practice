# Problem: 36. Valid Sudoku
# Link: https://leetcode.com/problems/valid-sudoku/


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        hashmap = {}
        # alternatively, use 3 sets to keep track of filled cells (filled row, column and box)

        # parse the input matrix
        for i in range(rows):
            for j in range(cols):
                # if the cell is filled
                if "1" <= board[i][j] <= "9":
                    # the number represents the key
                    key = board[i][j]
                    # the row of the filled cell
                    filled_row = str(i) + "r"
                    # the column of the filled cell
                    filled_col = str(j) + "c"
                    # the box of the filled cell (there are 9 sub-boxes in the grid)
                    box = str(i // 3) + str(j // 3)

                    # if the key is mapped
                    if key in hashmap:
                        # if any of the row, column or box were marked with this number before, the grid is not valid
                        if (
                            filled_row in hashmap[key]
                            or filled_col in hashmap[key]
                            or box in hashmap[key]
                        ):
                            return False
                        # otherwise map the key to the values
                        hashmap[key].extend([filled_row, filled_col, box])
                    else:
                        hashmap[key] = [filled_row, filled_col, box]

        # the grid is valid
        return True
