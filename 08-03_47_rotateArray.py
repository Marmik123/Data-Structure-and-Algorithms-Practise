class Solution(object):
    
            
        
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # sol=Solution()
        self.reverseElements(nums,0,len(nums)-1)
        self.reverseElements(nums,0,k-1)
        self.reverseElements(nums,k,len(nums)-1)
        
        
    def reverseElements(self,nums,start,end):
        start = start
        end = end
        while start<end:
            temp=nums[start]
            nums[start]=nums[end]
            nums[end]=temp
            start+=1
            end-=1    
                
            
            
            
            
        
            
            
            
