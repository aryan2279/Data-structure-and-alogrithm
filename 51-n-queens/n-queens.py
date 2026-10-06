class Solution:
    def solveNQueens(self, n):
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]

        def safe(row, col):

            # Check column
            for i in range(row - 1, -1, -1):
                if board[i][col] == 'Q':
                    return False

            # Check upper-left diagonal
            i = row - 1
            j = col - 1

            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            # Check upper-right diagonal
            i = row - 1
            j = col + 1

            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def place(row):

            if row == n:
                ans.append([''.join(r) for r in board])
                return

            for col in range(n):

                if safe(row, col):

                    # Place queen
                    board[row][col] = 'Q'

                    # Move to next row
                    place(row + 1)

                    # Backtrack
                    board[row][col] = '.'

        place(0)

        return ans