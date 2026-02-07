class Solution:
    def reverseString(self, s: List[str]) -> None:
                n = len(s)
                right = n//2
                for left in range(right):
                    s[left],s[n-left-1] =s[n-left-1],s[left]
                 
        