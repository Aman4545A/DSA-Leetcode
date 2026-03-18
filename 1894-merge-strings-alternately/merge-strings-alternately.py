class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        s = ""

        while(i<len(word1) and j<len(word2)):
            s = s + word1[i] + word2[j]
            i = i+1
            j = j+1

        while(j<len(word2)) :
            s = s+ word2[j]
            j = j+1

        while(i<len(word1)) :
            s = s+ word1[i] 
            i = i+1 


        return s        

        