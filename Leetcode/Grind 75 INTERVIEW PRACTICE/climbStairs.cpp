class Solution {
public:
    int climbStairs(int n) {
        if (n==1)
        {
            return 1;
        }

        if(n==2)
        {
            return 2;
        }

        int step1=1;
        int step2=2;
        int curstep=0;

        for (int i=2;i<n;i++) //start from i=2 , the third element
        {
            curstep=step1+step2;
            if (i%2==1) //odd update step2
            {
                step2=curstep; 
            }
            else //even update step1
            {
                step1=curstep; 
            }
            //cout<<curstep<<endl;
        }

        return curstep;
        
    }
};
