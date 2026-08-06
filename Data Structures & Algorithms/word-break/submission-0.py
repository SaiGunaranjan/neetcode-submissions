class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Code not working
        max_word_len = 0
        for word in wordDict:
            if len(word)>max_word_len:
                max_word_len = len(word)

        len_s = len(s)
        dp = [False]*(len_s+1)
        dp[0] = True

        for i in range(len_s):
            for word in wordDict:
                match_str = ''
                k = 0
                while k < max_word_len and (i>=k):
                    match_str = s[i-k] + match_str
                    if (match_str == word) and (dp[i-k] == True):
                        dp[i+1] = True
                    k += 1
                        
        return dp[-1]