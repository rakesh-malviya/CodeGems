# -*- coding: utf-8 -*-
"""Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substrings without repeating characters for “ABDEFGABEF” are “BDEFGA” 
and “DEFGAB”, with length 6. For “BBBB” the longest substring is “B”, with length 1. 
For “GEEKSFORGEEKS”, there are two longest substrings shown in the below diagrams, with length 7."""


def main(str1):
  n = len(str1) 
  lastIndexArr = [None]*n
  
  if n==0:
    return 0
  
  lastIndexMap = {}
  
  for i,c in enumerate(str1):
    lastIndex = lastIndexMap.get(c)
    lastIndexArr[i] = lastIndex
    lastIndexMap[c] = i
    
  max = 0
  for i in range(len(str1)):
    tempLen = 0
    for j in range(i,len(str1)):
      lastIndexOfJchar = lastIndexArr[j]
      if lastIndexOfJchar==None:
        tempLen+=1
      elif i<= lastIndexOfJchar and lastIndexOfJchar<=j:
        break
      else:
        tempLen+=1
        
    if max < tempLen:
      max = tempLen
      
  return max


def main2(str1):
  n = len(str1) 
  lastIndexArr = [None]*n
  
  if n==0:
    return 0,""
  
  lastIndexMap = {}
  
  for i,c in enumerate(str1):
    lastIndex = lastIndexMap.get(c)
    lastIndexArr[i] = lastIndex
    lastIndexMap[c] = i
    
  max_len = 0
  max_start = 0
  start = 0
  for end in range(1,len(str1)):
    endCharLastIndex = lastIndexArr[end]
    if endCharLastIndex!=None and start <= endCharLastIndex:
      start = endCharLastIndex + 1
    
    curLen = end - start + 1
    if max_len < curLen:
      max_len = curLen
      max_start = start
      
  return max_len,str1[max_start:max_start+max_len]

print (main("GEEKSFORGEEKS")) 
print (main("ABDEFGABEF"))         
      
print (main2("GEEKSFORGEEKS")) 
print (main2("ABDEFGABEF"))         
     
  
    