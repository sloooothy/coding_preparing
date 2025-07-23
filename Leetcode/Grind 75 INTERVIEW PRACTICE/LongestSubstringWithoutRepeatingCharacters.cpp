class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l=0;
        unordered_map<char,int> hashmap;
        int res=0;
        for (int r=0;r<s.size();r++)
        {


            while(hashmap[s[r]]>0) //already existed
            {
                // move left until s[r] is not replicate anymore
                hashmap[s[l]]-=1;
                l+=1;
            }

            hashmap[s[r]]+=1;
            res=max(res,r-l+1);
            
        
        }

        return res;
    }
};
