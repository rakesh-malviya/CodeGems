# -*- coding: utf-8 -*-
"""
Write an efficient C program to find the sum of contiguous subarray 
within a one-dimensional array of numbers which has the largest sum.
"""
def LSCS(arr):
  max_so_far = 0
  max_ending_here = 0
  
  for elem in arr:
    max_ending_here = max_ending_here + elem
    
    if max_ending_here<0:
      max_ending_here = 0
    
    if max_so_far < max_ending_here:
      max_so_far = max_ending_here
  
  return max_so_far

arr = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
print(LSCS(arr))
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(LSCS(arr))