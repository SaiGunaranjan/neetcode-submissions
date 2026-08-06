class Solution {
public:
    bool checkInclusion(string s1, string s2) {

        int n1 = s1.length();
        int n2 = s2.length();

        if (n1 > n2)
            return false;

        vector<int> indicator_s1(26,0);
        vector<int> indicator_s2(26,0);

        for (int i=0;i<n1;i++)
        {
            indicator_s1[s1[i]-'a'] += 1;
            indicator_s2[s2[i]-'a'] += 1;
        }

        if (indicator_s1 == indicator_s2)
            return true;

        int lp = 0;
        for (int rp=n1;rp<n2;rp++)
        {
            indicator_s2[s2[lp] - 'a'] -= 1;
            indicator_s2[s2[rp] - 'a'] += 1;

            if (indicator_s1 == indicator_s2)
                return true;

            lp += 1;
        }

        return false;


        
    }
};
