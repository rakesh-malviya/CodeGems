class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        table = [0]*n
        i=n-2
        while(i>=0):
          steps = nums[i]
          if steps==0:
            table[i] = n+99
          elif steps==1:
            table[i]=table[i+1]+1
          else:
              minVal = min(table[i+1:i+steps+1])              
              table[i] = minVal+1
            
#           print(table)
          i-=1
          
        if table[0]==n+99:
          return 0
        else:
          return table[0]
      
s = Solution()
print(s.jump([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))            
print(s.jump([1, 3, 5, 8, 9, 2, 6, 0, 6, 8, 9,0,0,0,0]))
print(s.jump([2,3,1]))
