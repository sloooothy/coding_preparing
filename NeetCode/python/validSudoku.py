class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ROWS,COLS=len(board),len(board[0])

        #check rows
        for r in range(ROWS):
            hashset=set()
            for c in range(COLS):
                if board[r][c] == '.':
                    continue
                if board[r][c] in hashset:
                    return False
                hashset.add(board[r][c])

        #check cols
        for c in range(COLS):
            hashset=set()
            for r in range(ROWS):
                if board[r][c] == '.':
                    continue
                if board[r][c] in hashset:
                    return False
                hashset.add(board[r][c])

        #3x3
        for R in range(0,9,3):
            for C in range(0,9,3):
                hashset=set()
                for r in range(R,R+3):
                    for c in range(C,C+3):
                        if board[r][c] == '.':
                            continue
                        if board[r][c] in hashset:
                            return False
                        hashset.add(board[r][c])
            
        return True
