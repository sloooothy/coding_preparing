class Solution {
public:
    string addBinary(string a, string b) {

        int carry=0;
        int sum=0;

        int pos_a=a.size()-1;
        int pos_b=b.size()-1;

        string res="";

        while(pos_a>=0 || pos_b>=0)
        {
            char a_digit=(pos_a>=0)?a[pos_a]:'0';
            char b_digit=(pos_b>=0)?b[pos_b]:'0';
            int A=(a_digit=='1')?1:0;
            int B=(b_digit=='1')?1:0;
            //XOR summing
            sum=(a_digit==b_digit)?0:1;
            //cout<<sum<<endl;
            //cout<<carry<<endl;
            sum=sum^carry;
            if(sum==0)
            {
                res='0'+ res;
            }
            else
            {
                res='1'+ res;
            }
            //carry if the sumation has carry for next term
            carry=(A+B+carry>1)?1:0;

            // update position pointer for a,b strings
            pos_a-=1;
            pos_b-=1;
        }

        if(carry)
        {
            res='1'+res;
        }

        return res;
        
    }
};
