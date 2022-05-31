"""
https://leetcode.com/problems/valid-sudoku/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:


Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check for row and col
        # if row => board[i][j], it can be transposed to become a column,
        # i.e. col=> board[j][i]
        for i in range(0, 9):  # hardcoding as its 9x9 matrix
            col_set = set()
            row_set = set()
            for j in range(0, 9):

                if board[i][j] != '.':
                    if board[i][j] in row_set:
                        return False
                    elif board[i][j] != '.':
                        row_set.add(board[i][j])

                if board[j][i] != '.':
                    if board[j][i] in col_set:
                        return False
                    elif board[j][i] != '.':
                        col_set.add(board[j][i])

                if i % 3 == 0 and j % 3 == 0:  # then its starting point of the 3x3 box
                    if not self.is_square_valid(board, i, j):
                        return False
        return True

    def is_square_valid(self, board, i, j):
        sq_set = set()
        for row in range(i, i + 3):
            for col in range(j, j + 3):
                if board[row][col] == '.':
                    continue
                if board[row][col] in sq_set:
                    return False
                else:
                    sq_set.add(board[row][col])
        return True



