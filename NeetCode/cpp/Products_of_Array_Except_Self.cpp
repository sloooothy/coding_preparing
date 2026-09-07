class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res;
        vector<int> prefix_num, postfix;
        int prod_cal=1;
        int i;
        for (i=0;i<nums.size();i++)
        {
            //cout<<prod_cal<<endl;
            prefix_num.push_back(prod_cal);
            prod_cal*=nums[i];
        }

        prod_cal=1;
        for (i=nums.size()-1;i>=0;i--)
        {
            //cout<<prod_cal<<endl;
            postfix.push_back(prod_cal);
            prod_cal*=nums[i];
        }

        for (i=0;i<nums.size();i++)
        {
            /*
            cout<<"("<<i<<")";
            cout<<prefix_num[i]<<"x";
            cout<<postfix[nums.size()-1-i]<<endl;
            */
            res.push_back(prefix_num[i]*postfix[nums.size()-1-i]);
            
        }
        

        return res;

    }
};
