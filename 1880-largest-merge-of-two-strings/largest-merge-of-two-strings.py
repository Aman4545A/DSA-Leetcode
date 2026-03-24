class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        s = []

        while i < len(word1) and j < len(word2):
            if word1[i:] > word2[j:]:
                s.append(word1[i])
                i += 1
            else:
                s.append(word2[j])
                j += 1

        while i < len(word1):
            s.append(word1[i])
            i += 1

        while j < len(word2):
            s.append(word2[j])
            j += 1

        return "".join(s)