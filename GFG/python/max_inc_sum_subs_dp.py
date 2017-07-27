
def MSIS(A,prev,id):
    if id >= len(A):
        return 0;
        
    cur = A[id]
    
    if cur > prev:
        return max(MSIS(A,cur,id+1)+cur,MSIS(A,prev,id+1))
    else:
        return MSIS(A,prev,id+1)
      
def MSIS_mem(A):
  
  table = {}
  n=len(A)
  table[-1] = [None for _ in range(n+1)]
  for i in A:
    table[i] = [None for _ in range(n+1)]
    
  r = _MSIS_mem(A,-1,0,table)
  return (r)
  
  
    
def _MSIS_mem(A,prev,id,table):
    if table[prev][id]!=None:
      return table[prev][id]
  
    r = None
    
    if id >= len(A):
        r = 0;
    
    else:    
      cur = A[id]
      
      if cur > prev:
          r = max(_MSIS_mem(A,cur,id+1,table)+cur,_MSIS_mem(A,prev,id+1,table))
      else:
          r = _MSIS_mem(A,prev,id+1,table)
          
    table[prev][id]=r  
    return r
  
  
      
A = [1, 101, 2, 3, 100, 4, 5]      
print(MSIS(A,-1,0))
print(MSIS_mem(A))
A = [10,5,3,1]      
print(MSIS(A,-1,0))
print(MSIS_mem(A))