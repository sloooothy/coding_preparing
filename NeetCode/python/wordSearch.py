class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS,COLS = len(board), len(board[0])
        path=set()

        def dfs(r,c,i):
            if i==len(word):
                return True
            if r<0 or c<0 or r>=ROWS or c>=COLS or word[i]!=board[r][c] or (r,c) in path:
               return False 

            path.add((r,c)) # add to set, don't go back if current path is moving on

            res=dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
            
            path.remove((r,c)) #the trace is done, go back and release the position r,c for new path searching

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):# walk m*n to check if it's the start of the word
                    return True
        return False


        
