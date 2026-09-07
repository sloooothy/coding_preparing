class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        ROW,COL=len(matrix),len(matrix[0])
        # row, col mark
        r_mark=[1]*ROW
        c_mark=[1]*COL

        for m in range(ROW):
            for n in range(COL):
                if matrix[m][n]==0:
                    r_mark[m]=0
                    c_mark[n]=0
        # set 0 according to marks
        for m in range(ROW):
            if r_mark[m]==0:
                for n in range(COL):
                    matrix[m][n]=0
        for n in range(COL):
            if c_mark[n]==0:
                for m in range(ROW):
                    matrix[m][n]=0
                
