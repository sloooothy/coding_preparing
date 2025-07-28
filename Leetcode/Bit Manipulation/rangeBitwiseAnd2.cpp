class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {

        //找出高位元共同前綴
        int shift=0;
        for (int i=0;i<32;i++) //計數： 同時記錄你總共「切掉」了多少位元 (即右移了多少次)。
        {
            //目標： 不斷地將 left 和 right 向右邊「切掉」位元，直到它們完全相同。
            if (left!=right)
            {
                left=left>>1;
                right=right>>1;
            }
            else
            {
                shift=i;
                break;
            }

        }

        return left<<shift; //還原： 當 left 和 right 相等時，這個值就是它們的最長共同前綴。將這個共同前綴向左移回「切掉的位元數」那麼多位，後面補 0
        
    }
};
