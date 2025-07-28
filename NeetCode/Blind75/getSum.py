class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        res=0
        carry=0

        for i in range(32):
            res = res | ( ((a & 1) ^ (b & 1) ^ carry)<<i)
            carry = ((a & 1) & (b & 1)) | ((a & 1) ^ (b & 1)) & carry
            a>>=1
            b>>=1


        MAX_INT = 0x7FFFFFFF # 2^31 - 1

        if res > MAX_INT: #處理Overflow
            res = ~(res ^ 0xFFFFFFFF) 


        return res
