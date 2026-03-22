class Solution:
    def compress(self, chars: List[str]) -> int:
        nums2 = []
        count = 1

        for i in range(len(chars) - 1):
            if chars[i] == chars[i + 1]:
                count += 1
            else:
                nums2.append(chars[i])
                if count > 1:
                    for digit in str(count):
                        nums2.append(digit)
                count = 1   

       
        nums2.append(chars[-1])
        if count > 1:
            for digit in str(count):
                nums2.append(digit)
            

       
        for i in range(len(nums2)):
            chars[i] = nums2[i]

        return len(nums2)