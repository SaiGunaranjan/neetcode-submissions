class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        
        indicator_s1 = [0]*26
        indicator_s2 = [0]*26

        for i in range(n1):
            indicator_s1[ord(s1[i]) - ord('a')] += 1
            indicator_s2[ord(s2[i]) - ord('a')] += 1

        if indicator_s1 == indicator_s2:
            return True

        lp = 0
        for rp in range(n1,n2):
            indicator_s2[ord(s2[lp]) - ord('a')] -= 1
            indicator_s2[ord(s2[rp]) - ord('a')] += 1

            if indicator_s1 == indicator_s2:
                return True

            lp += 1
        
        return False



        
        
        

