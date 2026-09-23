class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsCorrect = True
        colsCorrect = True
        squaresCorrect = True
        nums = set("123456789")
        for i in range(9):
            row = []
            col = []
            for j in range(9):
                ch_x = board[i][j]
                ch_y = board[j][i]
                if ch_x in nums:
                    row.append(int(ch_x))
                if ch_y in nums:
                    col.append(int(ch_y))

            # sprawdzanie cols i rows
            if len(row) != len(set(row)):
                rowsCorrect = False
            if len(col) != len(set(col)):
                colsCorrect = False

        # 3x3
        squares = [[] for _ in range(9)]
        for i in range(9):
            square = []
            for j in range(9):
                ch = board[i][j]
                if ch == '.':
                    continue

                square_index = (i//3) * 3 + (j//3)
                squares[square_index].append(ch)

        for square in squares:
            if len(square) != len(set(square)):
                squaresCorrect = False

        valid = squaresCorrect and rowsCorrect and colsCorrect
        return valid
        