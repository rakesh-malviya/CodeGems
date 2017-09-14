"""
Given a rod of length n inches and an array of prices that contains prices of all 
pieces of size smaller than n. Determine the maximum value obtainable by cutting 
up the rod and selling the pieces. For example, if length of the rod is 8 and the 
values of different pieces are given as following, then the maximum obtainable 
value is 22 (by cutting in two pieces of lengths 2 and 6)


length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 1   5   8   9  10  17  17  20

And if the prices are as following, then the maximum obtainable value is 24 
(by cutting in eight pieces of length 1)

length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 3   5   8   9  10  17  17  20
"""

def rodCut(P,L,n,id):
  m = len(L)
  if id>=m:
    return 0
    
  if n<=0:
    return 0
  
  if n-L[id]>=0:
    return max(
                  rodCut(P, L, n, id+1), #Not cut
                  rodCut(P, L, n-L[id], id)+P[id] # cut
              )
  else:
    return rodCut(P, L, n, id+1)
  
def rodCut2(P,L,n):
  if n<=0:
    return 0
  
  max_val = -9999999
  
  for i in range(len(L)):
    if n-L[i]>=0:
      tempPrice = P[i]+rodCut2(P, L, n-i-1)
      if tempPrice > max_val:
        max_val = tempPrice
    
  return max_val

def rodCutTable(P,L,n):
  m = len(L)
  table=[[0 for _ in range(m)] for _ in range(n+1)]
  
  for i in range(1,n+1):
    for j in range(m):
      withCurLen = 0
      if i-L[j]>=0:
        withCurLen = table[i-L[j]][j]+P[j]
        
      withoutCurLen = 0
      if j-1 >= 0:
        withoutCurLen = table[i][j-1]
      
      table[i][j] = max(withCurLen,withoutCurLen)
      
  return table[n][m-1]

def rodCutTable2(P,L,n):
  m = len(L)
  table = [0 for _ in range(n+1)]
  
  for i in range(m):
    curLen = L[i]
    curPrice = P[i]
    for j in range(curLen,n+1):
      if j-curLen >=0:
        table[j] = max(table[j],table[j-curLen]+curPrice)
      
  return table[n]
      

L = [1 ,  2,   3,   4,  5,   6,   7,   8]  
P = [1,   5,   8,   9,  10,  17,  17,  20]
print(rodCut(P, L, 8, 0))
print(rodCut2(P, L, 8))
print(rodCutTable(P, L, 8))
print(rodCutTable2(P, L, 8))

L = [1 ,  2,   3,   4,  5,   6,   7,   8]  
P = [3,   5,   8,   9,  10,  17,  17,  20]
print(rodCut(P, L, 8, 0))
print(rodCut2(P, L, 8))
print(rodCutTable(P, L, 8))
print(rodCutTable2(P, L, 8))
