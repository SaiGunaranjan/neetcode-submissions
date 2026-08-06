class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        dict_s = {}
        for char_s in s:
            if char_s in dict_s:
                dict_s[char_s] += 1
            else:
                dict_s[char_s] = 1
        
        
        for char_t in t:
            if char_t in dict_s:
                if dict_s[char_t] > 0:
                    dict_s[char_t] -= 1
                else:
                    return False
            else:
                return False

            
        return True

        
        
        
        



        