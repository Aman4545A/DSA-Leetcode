class Solution(object):
    def isPalindrome(self, s):
        result = ''.join(ch for ch in s if ch.isalnum()).lower()
        return result == result[::-1]
