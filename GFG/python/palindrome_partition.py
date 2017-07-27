import sys

def _minPalPart(arr,start,end):
  if start==end:
    return 0,True
  
  if start==end+1:
    if arr[start]==arr[end]:
      return 0,True
    else:
      return 1,False
  
  else:
    palpart_startp1_endm1,isPalpart = _minPalPart(arr, start+1, end-1)
    if isPalpart==True and arr[start]==arr[end]:
      return 0,True
    else:
      minVal = sys.maxint
      for k in range(start+1,end):
        palpart_start_k,isPal_start_k = _minPalPart(arr, start, k)
        palpart_kp1_end,isPal_kp1_end = _minPalPart(arr, k+1, end)
        tempVal = palpart_start_k + palpart_kp1_end + 1
        
        if tempVal < minVal:
          minVal = tempVal
          
      return minVal,False

def minPalPart(arr):
  n=len(arr)
  if n==0:
    return 0
  return _minPalPart(arr, 0, n-1)

def _minPalPartTable(arr,start,end,tablePart,tableIsPal):
  if tableIsPal[start][end]!=None and tablePart[start][end]!=None:
    return tablePart[start][end],tableIsPal[start][end]
  
  if start==end:
    tableIsPal[start][end]=True
    tablePart[start][end]=0
    return 0,True
  
  if start==end+1:
    if arr[start]==arr[end]:
      tableIsPal[start][end]=True
      tablePart[start][end]=0
      return 0,True
    else:
      tableIsPal[start][end]=False
      tablePart[start][end]=1
      return 1,False
  
  else:
    palpart_startp1_endm1,isPalpart = _minPalPartTable(arr, start+1, end-1,tablePart,tableIsPal)
    if isPalpart==True and arr[start]==arr[end]:
      return 0,True
    else:
      minVal = sys.maxint
      for k in range(start+1,end):
        palpart_start_k,isPal_start_k = _minPalPartTable(arr, start, k,tablePart,tableIsPal)
        palpart_kp1_end,isPal_kp1_end = _minPalPartTable(arr, k+1, end,tablePart,tableIsPal)
        tempVal = palpart_start_k + palpart_kp1_end + 1
        
        if tempVal < minVal:
          minVal = tempVal
          
      tableIsPal[start][end]=False
      tablePart[start][end]=minVal
      return minVal,False

def minPalPartTable(arr):
  n=len(arr)
  if n==0:
    return 0
  tableIsPal = [[None for _ in range(n)] for _ in range(n)]
  tablePart = [[None for _ in range(n)] for _ in range(n)]
  return _minPalPartTable(arr, 0, n-1,tablePart,tableIsPal)

arr=""
print(minPalPart(arr))
arr="babab"
print(minPalPart(arr))
arr="ababbb"
print(minPalPart(arr))
arr="ababbbabbababa"
print(minPalPart(arr))

arr=""
print(minPalPartTable(arr))
arr="babab"
print(minPalPart(arr))
arr="ababbb"
print(minPalPartTable(arr))
arr="ababbbabbababa"
print(minPalPartTable(arr))