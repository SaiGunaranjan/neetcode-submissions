class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        
        lp = 0
        s_dict = {s[0]:0}
        max_len = 1
        for rp in range(1,len(s)):
            if (s[rp] in s_dict) and (s_dict[s[rp]] >= lp):
                lp = s_dict[s[rp]] + 1
            s_dict[s[rp]] = rp
            max_len = max(max_len,rp-lp+1)
        return max_len


            
