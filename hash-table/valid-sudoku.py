class Solution(object):
    def isValidSudoku(self, board):
        def isvalid(arr):
            new=[]
            for i in arr:
                if i==".":
                    pass
                else:
                    if i not in new:
                        new.append(i)
                    else:
                        return False
            return True
        for i in range(9):
            if isvalid(board[i]):
                pass
            else:
                return False
        i=0
        for i in range(9):
            column=[]
            for z in range(9):
                column.append(board[z][i])
            if isvalid(column):
                pass
            else:
                return False
        i=0
        for g in range(3):
            for k in range(3):
                block=[]
                for i in range(3):
                    for j in range(3):
                        block.append(board[i+g*3][j+k*3])
                if isvalid(block):
                    pass
                else :
                    return False
        return True