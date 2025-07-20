class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        
        for i in range(n+1):
            ans_i=0
            while(i>0):
                ans_i+=i%2
                i//=2
            res.append(ans_i)
                
        return res