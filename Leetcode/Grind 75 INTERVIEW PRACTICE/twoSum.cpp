class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> prevElement;

        for (int i=0;i<nums.size();i++)
        {
            int dif=target-nums[i];
            if(prevElement.count(dif))
            {
                return {prevElement[dif],i};
            }

            prevElement[nums[i]]=i;

        }

        return {0,0};
    }
};
