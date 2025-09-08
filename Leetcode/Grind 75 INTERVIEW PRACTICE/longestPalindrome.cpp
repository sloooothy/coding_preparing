class Solution {
public:
    string curPosStr(int l,int r,string os)
    {
        while (l>=0 && r<os.size() && os[l]==os[r])
        {
            l-=1;
            r+=1;
        }

        string curres="";
        for (int j=l+1;j<r;j++)
        {
            curres+=os[j];
        }
        return curres;

    }
    string longestPalindrome(string s) {
        string res="";
        string cur="";
        for (int i=0;i<s.size();i++)
        {
            //odd length
            cur=curPosStr(i,i,s);
            if(cur.size()>res.size())
            {
                res=cur;
            }

            //even length
            cur=curPosStr(i,i+1,s);
            if(cur.size()>res.size())
            {
                res=cur;
            }

        }


        return res;


    }
};
