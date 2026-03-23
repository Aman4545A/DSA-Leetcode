class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        
        for i in range(len(arr1)):
            valid = True   
            
            j = 0
            while j < len(arr2):
                if abs(arr1[i] - arr2[j]) <= d:
                    valid = False
                    break   
                
                j += 1
            
            if valid:
                count += 1
        
        return count