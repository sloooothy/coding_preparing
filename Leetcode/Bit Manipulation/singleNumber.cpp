class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res=0;

        // 外層迴圈：遍歷所有可能的位元位置 (從第 0 位到第 31 位)
        for (int b = 0; b < 32; b++) { //int 32位
            int sum_of_bits = 0; // 紀錄當前位元位置上 '1' 的總次數

            // 內層迴圈：遍歷 nums 陣列中的每一個數字
            for (int num : nums) { 
                // 檢查當前數字在 'b' 位元位置上是否為 1
                // num >> b 的最尾位 如果是1則加入
                sum_of_bits+=( num >> b ) & 1 ;
            }
            //加完之後 mod3 確定餘 再加回原位元
            res |= ((sum_of_bits%3)<<b);
            
        }

        return res;
    }
};
