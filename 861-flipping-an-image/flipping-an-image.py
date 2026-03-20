from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
          
        for i in range(len(image)):
            for j in range(len(image[i])):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0

        
        for row in image:
            row.reverse()

        return image  


        