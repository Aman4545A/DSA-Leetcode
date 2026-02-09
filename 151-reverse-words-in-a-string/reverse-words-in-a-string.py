class Solution:
    def reverseWords(self, s: str) -> str:

                s=s.split()
                n = len(s)
                mid = len(s)//2

                for i in range(mid):
                    temp = s[i]
                    s[i]= s[n-i-1]
                    s[n-i-1]=temp
                    
                new_string = " ".join(s)
                return new_string


   
    
        