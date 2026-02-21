class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
                s = list(s) 
                i = 0 
                j = len(s)-1

                while(i<j):
                    if(s[i].isalpha() and s[j].isalpha()):
                        s[i] , s[j] = s[j], s[i]
                        i = i+1
                        j = j-1
                        
                    elif (not s[i].isalpha() and s[j].isalpha()):
                        i = i+1
                        
                    elif(not s[j].isalpha() and s[i].isalpha()):
                       j = j-1    
                        
                    else :
                        i = i+1
                        j = j-1
                        
                s = "".join(s)     
                return s
        