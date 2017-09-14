# -*- coding: utf-8 -*-
""" 
  {{0, 1, 1, 0, 1}, 
   {1, 1, 0, 1, 0}, 
   {0, 1, 1, 1, 0},
   {1, 1, 1, 1, 0},
   {1, 1, 1, 1, 1},
   {0, 0, 0, 0, 0}};
  
  {{00, 11, 12, 00, 11}, 
   {11, 22, 00, 11, 00}, 
   {00, 13, 21, 32, 00},
   {11, 24, 32, 43, 00},
   {12, 25, 33, 44, 51},
   {00, 00, 00, 00, 00}};

  {{00, 11, 12, 00, 11}, 
   {11, 22, 00, 11, 00}, 
   {00, 13, 21, 32, 00},
   {11, 24, 32, 43, 00},
   {12, 25, 33, 44, 51},
   {00, 00, 00, 00, 00}};

   
"""

def maxSquareSize(mat):
  newMat = [[y for y in x] for x in mat]
  
  def get(tempMat,r,c):
    try:
      return tempMat[r][c]
    except:
      return 0
  
  for i in range(1,len(newMat)):
    for j in range(1,len(newMat[0])):
      dia = get(newMat,i-1,j-1)
      rt = get(newMat,i-1,j)
      up =  get(newMat,i,j-1)
      if mat[i][j]==1:
        newMat[i][j] = min(dia,rt,up) + 1
      else:
        newMat[i][j] = 0
        
  val = max(max(x) for x in newMat)
  return val*val

mat = [[0, 1, 1, 0, 1], 
       [1, 1, 0, 1, 0], 
       [0, 1, 1, 1, 0],
       [1, 1, 1, 1, 0],
       [1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0]]

print(maxSquareSize(mat))
                
        
    
    
    