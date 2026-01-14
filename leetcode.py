#finding the longest common prefix in a list of strings
class Solution:
    def longestCommonPrefix(self, strs):
        string = strs
        if not string:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
         while not s.startswith(prefix):
            prefix = prefix[::-1]
            if not prefix:
                return ""
        return prefix

