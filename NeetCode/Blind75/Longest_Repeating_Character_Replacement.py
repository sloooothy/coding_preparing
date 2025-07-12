class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        word_cnt=defaultdict(int) #storing character frequency
        max_freq=0 #save the max frequency, check by each new character added
        long_rep=0 #final answer
        l,r=0,0 #left,right pointer
        for r in range(len(s)):
            word_cnt[s[r]]+=1 #record frequency for each new character
            max_freq=max(max_freq,word_cnt[s[r]]) #update max frequency

            while(r-l+1-max_freq>k): #if the current sliding windows can't adapt the constraint k
                #reduce the frequency and  move left pointer
                word_cnt[s[l]]-=1
                l+=1 
            
            long_rep=max(long_rep,r-l+1) #when k constraint is meet, update answer

        return long_rep
            