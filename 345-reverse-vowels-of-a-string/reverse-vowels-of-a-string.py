class Solution:
    def reverseVowels(self, s: str) -> str:
        temp = list(s)
        n = len(temp)

        left = 0
        right = n - 1

        while left < right:
            if temp[left] not in "aeiouAEIOU":
                left += 1
            elif temp[right] not in "aeiouAEIOU":
                right -= 1
            else:
                temp[left], temp[right] = temp[right], temp[left]
                left += 1
                right -= 1

        s = "".join(temp)
        return s
        