class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_set<char> check_dbl;

        for (int i=0;i<9;i++)
        {
            for(int j=0;j<9;j++)
            {
                if (board[i][j]!='.')
                {
                    check_dbl.clear();
                    for(int k=0;k<9;k++)
                    {
                        if(check_dbl.count(board[i][k])!=0) // i fix
                        {
                            //cout<< "i fix"<<endl;
                            return false;
                        }
                        else{
                            if (board[i][k]!='.'){
                                check_dbl.insert(board[i][k]);
                            }
                                
                        }
                    }

                    check_dbl.clear();
                    for(int k=0;k<9;k++)
                    {
                        
                        if(check_dbl.count(board[k][j])!=0) // j fix
                        {
                            //cout<< "j fix"<<endl;
                            return false;
                        }
                        else{
                            if (board[k][j]!='.'){
                                check_dbl.insert(board[k][j]);
                            }
                                
                        }
                    }

                    int mi=i/3;
                    int mj=j/3;
                    //cout<<mi<<","<<mj<<endl;
                    check_dbl.clear();
                    for(int gi=mi*3;gi<mi*3+3;gi++){
                        for(int gj=mj*3;gj<mj*3+3;gj++)
                        {
                            if(check_dbl.count(board[gi][gj])!=0) //3x3
                            {
                                //cout<< "3x3"<<endl;
                                return false;
                            }
                            else{
                                if (board[gi][gj]!='.'){
                                    check_dbl.insert(board[gi][gj]);
                                }
                                    
                            }
                        }
                    }

                }


            }
        }

        return true;
        
    }
};
