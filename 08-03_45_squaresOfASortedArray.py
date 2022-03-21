class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer=[0]*len(nums)
        l=0
        r=len(nums)-1
        while l<=r:
            left,right=abs(nums[l]),abs(nums[r])
            if left>right:
                answer[r-l]=left*left
                l+=1
            else:
                answer[r-l]=right*right
                r-=1
        return answer   