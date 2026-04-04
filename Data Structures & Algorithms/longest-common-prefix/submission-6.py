class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    
        for i in range(len(strs[0])):
            for s in strs:
                if s:
                    continue
                else:
                    return""
                    if s[i] != strs[0][i]:
                        return s[0:i]
        return strs[0]

# traverse all strs
# traverse all works in strs
# if not correct, return the res
# if all are matched, return the first string
