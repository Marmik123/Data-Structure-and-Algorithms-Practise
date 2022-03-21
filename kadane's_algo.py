#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        max_so_far = -1e7
        max_ending_here = 0
        isAllNeg=False
        negCount=0
        for i in range(0,N):
        #     max=arr[i]
        #     while arr[i]<0:
        #         if arr[i]>max:
        #             max=arr[i]
        #         return max
            max_ending_here = max_ending_here+arr[i]
            if max_ending_here < 0:
                max_ending_here = 0
            if max_so_far < max_ending_here:
                max_so_far =  max_ending_here
        for i in range(N):
            if arr[i]<0:
                negCount+=1
        if negCount==N:
            max_so_far=arr[0]
            for i in range(N):
                if arr[i]>max_so_far:
                    max_so_far=arr[i]
            return max_so_far        
                
                
                
                
        return max_so_far    
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends