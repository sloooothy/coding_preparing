class Solution {
public:
    bool isValid(string s) {
        stack<char> chkparentheses;

        for (int i=0;i<s.size();i++)
        {
            if(s[i]=='(' || s[i]=='[' || s[i]=='{')
            {
                chkparentheses.push(s[i]);
            }
            else if (!chkparentheses.empty())
            {
                if (s[i]==')')
                {
                    if (chkparentheses.top()=='(')
                    {
                        chkparentheses.pop();
                    }
                    else
                    {
                        return false;
                    }
                }

                if (s[i]==']')
                {
                    if (chkparentheses.top()=='[')
                    {
                        chkparentheses.pop();
                    }
                    else
                    {
                        return false;
                    }
                }

                if (s[i]=='}')
                {
                    if (chkparentheses.top()=='{')
                    {
                        chkparentheses.pop();
                    }
                    else
                    {
                        return false;
                    }
                }


            }
            else{
                return false;
            }


        }

        return (chkparentheses.empty());


    }
};
