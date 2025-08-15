class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS,COLS=len(heights),len(heights[0])
        p1,p2=set(),set()

        def dfs(r,c,visitset,prevHt): # search reachable position
            if (r,c) in visitset or (r<0 or c<0 or r>ROWS-1 or c>COLS-1) or heights[r][c]<prevHt:
                return 
            # visit ok
            visitset.add((r,c))
            dfs(r-1,c,visitset, heights[r][c]) 
            dfs(r+1,c,visitset, heights[r][c]) 
            dfs(r,c-1,visitset, heights[r][c]) 
            dfs(r,c+1,visitset, heights[r][c]) 
        
        #p1,p2 search => by cols and rows
        for c in range(COLS):
            dfs(0,c,p1, heights[0][c]) 
            dfs(ROWS-1,c,p2, heights[ROWS-1][c])
          
        for r in range(ROWS):
            dfs(r,0,p1, heights[r][0]) 
            dfs(r,COLS-1,p2, heights[r][COLS-1])
        
        #find set union
        res=[]
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in p1 and (r,c) in p2:
                    res.append([r,c])


        return res
