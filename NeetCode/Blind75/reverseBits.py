class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        bits=31
        for i in range(32):
            res=res<<1
            res+=n%2
            #print(res)
            n=n//2
            

        return res
