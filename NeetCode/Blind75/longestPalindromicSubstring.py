class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        resLen=0

        #回文最長可能是奇數也可能是偶數字串，都要檢查
        for pos in range(len(s)): # each character as center
            #Odd length
            l,r=pos,pos
            #     [boundary case]         [pandrom]
            while l>=0 and r<len(s) and s[l]==s[r]:
                # extend palindromes while it's correct
                substr=s[l:r+1]
                if len(substr)>resLen:
                    res=substr
                    resLen=len(substr)
                l-=1
                r+=1

            #Even length
            l,r=pos,pos+1
            #     [boundary case]         [pandrom]
            while l>=0 and r<len(s) and s[l]==s[r]:
                # extend palindromes while it's correct
                substr=s[l:r+1]
                if len(substr)>resLen:
                    res=substr
                    resLen=len(substr)
                l-=1
                r+=1

        return res

