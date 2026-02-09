class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
                print("")
        else:
            prefix = strs[0]   

            for word in strs[1:]:

                i = 0
                while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
                     i += 1

                prefix = prefix[:i]   

                if prefix == "":
                    break

            return prefix
        