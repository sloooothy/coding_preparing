class Solution {
   public:
    char sep_code = '%';

    string encode(vector<string>& strs) {
        string encodeWord = "";
        for (int i = 0; i < strs.size(); i++) {
            encodeWord += to_string(strs[i].size()) + sep_code + strs[i];
        }
        cout << encodeWord << endl;
        return encodeWord;
    }

    vector<string> decode(string s) {
        vector<string> res;
        string newWord = "";
        int i = 0, j = 0, len_i;
        for (i = 0; i < s.size(); i++) {
            if (s[i] != sep_code) {
                j += 1;
            } else {
                string len = s.substr(i - j, j);
                // cout<<len<<endl;
                len_i = stoi(len);
                // cout<<len_i<<endl;
                // cout<<i+1<<","<<i+len_i<<endl;
                string recstr = s.substr(i + 1, len_i);
                res.push_back(recstr);

                i += (len_i);  // jump to the index after the string
                j = 0;
            }
        }

        return res;
    }
};
