class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {

        int max_word_len = 0;
        for (int i=0;i<wordDict.size();i++)
        {
            if (wordDict[i].length()>max_word_len)
            {
                max_word_len = wordDict[i].length();
            }
        }

        int len_s = s.length();
        vector<bool> dp(len_s+1,false);
        dp[0] = true;
        
        for (int i=0;i<len_s;i++)
        {
            for (std::string& word: wordDict)
            {
                std::string match_str = "";
                int k=0;
                while ((k < max_word_len) && (i>=k))
                {
                    match_str = s[i-k] + match_str;
                    if ((match_str == word) && (dp[i-k]==true))
                    {
                        dp[i+1] = true;
                    }
                    k += 1;
                }
            }
        }
        return dp[len_s];
        
    }
};
