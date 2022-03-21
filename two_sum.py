class Solution(object):
    #LEET CODE PROBLEM L TIME COMP:O(n^2)
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(0,len(nums)-1):
            if i+1 == len(nums)-1:
                j = i+1
                if nums[i]+nums[j]==target:
                    return [i,j]
            else:
                for j in range(i+1,len(nums)-1):
                    if nums[i]+nums[j]==target:
                        return [i,j]

#TIME EFFICIENT ALGO:  O(N)                
def  twoSumEff(arr,n,target):
    seen = {}
    for i,value in enumerate(arr):
        required = target - arr[i]
        
        if required in seen:
            return [i,seen[required]]
        seen[value]=i    

