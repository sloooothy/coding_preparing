class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        vector<int> mag_cnt= vector<int>(26);

        for (auto c:magazine)
        {
            int pos = int(c-'a');
            mag_cnt[pos]+=1;
        }

        for (auto c:ransomNote)
        {
            int char_pos= int(c-'a');
            if (mag_cnt[char_pos]==0)
            {
                return false;
            }
            else
            {
                mag_cnt[char_pos]-=1;
            }
                
        }



        return true;
        
    }
};
