# -*- coding: utf-8 -*-
"""
Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn�t matter.
For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. 
So output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are five solutions: 
{2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.
"""

def getChange(change,coins,str1=[],prev=-1):
  sum = 0
  for coin in coins:
    if coin<prev:
      continue
    minus = change-coin
    if minus == 0:
      sum+=1
      print(str1+[coin])
    elif minus > 0:
      sum+= getChange(minus, coins,str1+[coin],prev=coin)
  
  return sum

def getChangeTable(n,coins):
  m = len(coins)
  table = [[0 for _ in range(m)] for _ in range(n+1)]
  
  for j in range(m):
    table[0][j] = 1
    
  for i in range(1,n+1):
    for j in range(m):
      curCoin = coins[j]
      withCurCoin = 0
      if i - curCoin>=0:
        withCurCoin = table[i-curCoin][j]
        
      withoutCurCoin = 0
      if j-1>=0:
        withoutCurCoin = table[i][j-1]
        
      table[i][j] = withCurCoin + withoutCurCoin
      
  return table[n][m-1]

def getChangeTable2(n,coins):
  m = len(coins)
  
  table = [0 for _ in range(n+1)]
  table[0] = 1
  
  for i in range(m):
    curCoin = coins[i]
    for j in range(curCoin,n+1):
      table[j] += table[j-curCoin]
       
  return table[n]
      

change=4
coins=[1,2,3]
print(getChange(change, coins))
print(getChangeTable(change, coins))
print(getChangeTable2(change, coins))
change=60
coins=[2,5,3,6]
coins=[12,15,322,6]
print(getChange(change, coins))
print(getChangeTable(change, coins))
print(getChangeTable2(change, coins))
      
      
      
      
  