class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        nLen=len(s)
        hashset=deque()
        long_len=0

        for r in range(nLen):
            while(s[r] in hashset):
                hashset.popleft()
                l+=1
            
            hashset.append(s[r])
            r+=1

            long_len=max(long_len,r-l)

        return long_len
