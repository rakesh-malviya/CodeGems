# -*- coding: utf-8 -*-
"""
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. 
The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, � shows the first 11 ugly numbers. 
By convention, 1 is included.
"""

def ugly_numbers(n):
  
  ugly = [0]*n  
  ugly[0] = 1
  i2 = i3 = i5 = 0
  
  for i in range(1,n):
    nu2 = ugly[i2]*2
    nu3 = ugly[i3]*3
    nu5 = ugly[i5]*5    
    nu = min(nu2,nu3,nu5)
    ugly[i] = nu
    
    if(nu==nu2):
      i2 += 1
    if(nu==nu3):
      i3 += 1    
    if(nu==nu5):
      i5 += 1
    
    
  return ugly[-1]

print(ugly_numbers(150))
