class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1:
            return strs[0]

        longest_common_prefix = strs[0]
        if len(longest_common_prefix) == 0:
            return longest_common_prefix
        
        for ind in range(1,len(strs)):
            curr_str = strs[ind]
            if len(curr_str) > len(longest_common_prefix):
                curr_str = curr_str[0:len(longest_common_prefix)]
            else:
                longest_common_prefix = longest_common_prefix[0:len(curr_str)]
            for ele in range(len(longest_common_prefix)):
                if longest_common_prefix[ele] != curr_str[ele]:
                    if ele == 0:
                        return ""
                    else:
                        longest_common_prefix = longest_common_prefix[0:ele]
                        break

        return longest_common_prefix

        