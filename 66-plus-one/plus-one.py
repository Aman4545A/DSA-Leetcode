class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
                    
                    s = len(digits)

                    for i in range(s-1, -1, -1):
                        p = digits[i] % 10
                        q = digits[i] // 10
                        
                        if (p == 9 and q == 0):
                            digits[i] = 0
                            
                        elif (p == 9 and q > 0):
                            q = digits[i] + 1
                            digits[i] = q
                            break
                    
                        else:
                            r = digits[i] + 1
                            digits[i] = r
                            break

                    
                    if digits[0] == 0:
                        digits.insert(0, 1)

                    return digits