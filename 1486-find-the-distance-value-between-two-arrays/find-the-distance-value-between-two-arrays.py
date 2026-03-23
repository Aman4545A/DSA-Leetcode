from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        count = 0

        for i in range(len(arr1)):
            st = 0
            end = len(arr2) - 1
            valid = True

           
            while st <= end:
                mid = (st + end) // 2

                if abs(arr1[i] - arr2[mid]) <= d:
                    valid = False
                    break
                elif arr2[mid] < arr1[i]:
                    st = mid + 1
                else:
                    end = mid - 1

            if valid:
                count += 1

        return count       





    