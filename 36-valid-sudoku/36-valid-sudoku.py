class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row checker
        for i in range(0, 9):
            n = {}
            for j in range(0, 9):
                if board[i][j] != ".":
                    if board[i][j] in n:
                        return False
                    else:
                        n[board[i][j]] = 1
                    
        # col checker
        for i in range(0, 9):
            n = {}
            for j in range(0, 9):
                if board[j][i] != ".":
                    if board[j][i] in n:
                        return False
                    else:
                        n[board[j][i]] = 1
                        
        # grid checker
        # check each square
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                n = {}
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if board[k][l] != ".":
                            if board[k][l] in n:
                                return False
                            else:
                                n[board[k][l]] = 1
        return True