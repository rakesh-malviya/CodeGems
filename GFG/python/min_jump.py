class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
          return 0,None
        if nums[0]==0:
          return 0,None
        
        maxSteps=nums[0]
        prevJump=nums[0]
        steps=maxSteps
        jumpSteps=[prevJump]     
        jumps=1   
        i = 1
        while(i<len(nums)):
          if i==len(nums)-1:
            jumpSteps.append(nums[len(nums)-1])
            return jumps,jumpSteps
          
          if maxSteps < i+nums[i]:
            maxSteps=i+nums[i]
            prevJump = nums[i]
            
          steps -= 1
          
          if steps==0:
            jumps+=1
            jumpSteps.append(prevJump)
            if i>=maxSteps:
              return 0,None
            
            steps=maxSteps - i
            
          i+=1
        
        maxSteps = nums

          
s = Solution()
print(s.jump([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))            
print(s.jump([1, 3, 5, 8, 9, 2, 6, 0, 6, 8, 9,0,0,0,0]))
print(s.jump([2,3,1]))
