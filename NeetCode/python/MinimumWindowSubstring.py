from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_cnt=defaultdict(int) 
        t_len=len(t)
        min_len=float("inf")
        res=""
        need_len=0

        #count t char => what we need
        for t_i in range(t_len):
           t_cnt[t[t_i]]+=1 
        
        l,r=0,0
        need_cnt=defaultdict(int) 
        for r in range(len(s)):
            need_cnt[s[r]]+=1

            if s[r] in t_cnt and need_cnt[s[r]]<t_cnt[s[r]]:
                need_len+=1

            while need_len==t_len:
                if(r-l+1 < min_len):
                    min_len=r-l+1
                    res=s[l:r+1]
                    
                if s[l] in t_cnt and need_cnt[s[l]] == t_cnt[s[l]]:
                    need_len-=1

                need_cnt[s[l]]-=1
                l+=1

        return res