class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        M,N = len(matrix), len (matrix[0])
        fix_r=0

        for r in range(M):
            if target>=matrix[r][0] and target<=matrix[r][N-1]:
                fix_r=r

        l,r=0,N-1

        while l<=r:
            mid=(l+r)//2
            if matrix[fix_r][mid]==target:
                return True
            elif matrix[fix_r][mid]>target:
                r=mid-1
            else:
                l=mid+1

        return False
