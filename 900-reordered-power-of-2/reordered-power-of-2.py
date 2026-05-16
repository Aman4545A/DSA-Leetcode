class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = sorted(str(n))
        
        for i in range(31):
            if sorted(str(2**i)) == s:
                return True
                
        return False
        