# -*- coding: utf-8 -*-
"""
LCS for input Sequences �ABCDGH� and �AEDFHR� is �ADH� of length 3.
LCS for input Sequences �AGGTAB� and �GXTXAYB� is �GTAB� of length 4
"""
from pprint import pprint

def LCS(s1,s2):
  m = len(s1)
  n = len(s2)
  table = [[0]*(n+1) for _ in range(m+1)]
  pathMat = [[None]*(n+1) for _ in range(m+1)]
  
  for i in range(1,m+1):
    for j in range(1,n+1):
      if s1[i-1]==s2[j-1]:
        table[i][j] = 1 + table[i-1][j-1]
        pathMat[i][j] = 'd'
      else:
        table[i][j] = max(table[i-1][j],table[i][j-1])
        if table[i][j] == table[i-1][j]:          
          pathMat[i][j] = 'u'
        else:
          pathMat[i][j] = 'l'
  
  count = table[m][n]
  tempList = [None]*count
  i=m
  j=n
  while(count>0):       
    if pathMat[i][j]=='d':
      tempList[count-1]=s1[i-1]
      i-=1
      j-=1
      count-=1
    elif pathMat[i][j]=='u':
      i-=1
    elif pathMat[i][j]=='l':
      j-=1
    
  return "".join(tempList)
    
  return table[m][n]
        

X = "AGGTAB"
Y = "GXTXAYB"
print(LCS(X,Y))

X = "ABCDGH"
Y = "AEDFHR"
print(LCS(X,Y))