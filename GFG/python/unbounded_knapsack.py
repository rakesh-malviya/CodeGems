# -*- coding: utf-8 -*-
"""
Given a list of  integers, , and another integer,  
representing the expected sum. 
Select zero or more numbers from  such that the sum of 
these numbers is as near as possible, 
but not exceeding, to the expected sum ().
"""
import sys
sys.setrecursionlimit(15000)

def _unb_knapsack(arr,i,k,sum):
  
  if k==0:
    return sum
  if k < 0:
    return -1
  if i >=len(arr):
    return sum
  return max(_unb_knapsack(arr,i,k-arr[i],sum+arr[i]),_unb_knapsack(arr,i+1,k,sum))

def unb_knapsack(arr,k):
  return _unb_knapsack(arr,0,k,0)
  
print(unb_knapsack([1, 6, 9],12))
print(unb_knapsack([3, 4, 4, 4, 8],9))
print(unb_knapsack([2, 4],9))
print(unb_knapsack([2]*2000,1))