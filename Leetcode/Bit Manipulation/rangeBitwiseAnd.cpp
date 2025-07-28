class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {

        //Brian Kernighan's Algorithm
        while(right>left){
            right = right & right-1;
        }

        return right;
        
    }
};
