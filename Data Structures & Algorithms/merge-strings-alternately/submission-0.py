class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        len_word1 = len(word1)
        len_word2 = len(word2)
        if len_word1 > len_word2:
            word_len = len_word2
            res_string = word1[len_word2::]
        elif len_word1 < len_word2:
            word_len = len_word1
            res_string = word2[len_word1::]
        else:
            word_len = len_word1
            res_string = ''
        
        concat_str = ''
        for ele in range(word_len):
            concat_str += word1[ele]
            concat_str += word2[ele]
        
        return concat_str + res_string

            
        