"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int):
        i = 1
        j = z
        result = []

        while i <= z and j > 0:
            value = customfunction.f(i, j)

            if value == z:
                result.append([i, j])
                i += 1
                j -= 1

            elif value < z:
                i += 1   

            else:
                j -= 1   

        return result    
             
