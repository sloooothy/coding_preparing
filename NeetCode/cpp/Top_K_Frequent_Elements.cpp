class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        //count appearance
        map<int,int> cntmap;
        for (int ele:nums)
        {
            cntmap[ele]+=1;
        }
        //place in cnting order
        vector<vector<int>> cntorder(nums.size()+1);
        for (auto n:cntmap)
        {
            cntorder[n.second].push_back(n.first);
        }

        vector<int> res;

        for (int i=cntorder.size()-1;i>=0;i--)
        {
            if (cntorder[i].size()<=k)
            {
                for (int e:cntorder[i])
                {
                    res.push_back(e);
                    k-=1;
                }
            }

            
            if(k<0)
            {
                break;
            }
            
        }
        
        
        
        
        return res;
    }
};
