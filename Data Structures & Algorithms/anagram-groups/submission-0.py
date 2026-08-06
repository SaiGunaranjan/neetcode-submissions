class Solution:

    def isAnagram(self,s,t):
        if len(s) != len(t):
         return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if sorted_s == sorted_t:
            return True
        else:
            return False

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        len_array = len(strs)
        visited_ind = []
        output_list = []
        for ind1,string1 in enumerate(strs):
            if ind1 not in visited_ind:
                grouped_anagrams = [string1]
                if ind1 == len_array-1:
                    output_list.append(grouped_anagrams)
                    break
                else:
                    for ind2 in range(ind1+1,len_array):
                        if ind2 in visited_ind:
                            continue
                        else:
                            string2 = strs[ind2]
                            flag = self.isAnagram(string1,string2)
                            if flag == True:
                                visited_ind.append(ind2)
                                grouped_anagrams.append(string2)
            
                output_list.append(grouped_anagrams)

        return output_list

        
