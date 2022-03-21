#User function Template for python3
class Solution:
    #TRIPLET SUM INSIDE AN ARRAY.
    #Function to find if there exists a triplet in the 
    #array A[] which sums up to X.
    def find3Numbers(self,A, n, X):
        # Your Code Here
        A.sort()
        for i in range(n-2):
            # first_ele = A[i]
            left = i+1
            right = n-1
            while left<right:
                if A[left]+A[right]+A[i]==X:
                    return True
                elif A[left]+A[right]+A[i]>X:
                    right-=1
                elif A[left]+A[right]+A[i]<X:
                    left+=1
            
        return False
                
        
            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,X=map(int,input().strip().split())
        A=list(map(int,input().strip().split()))
        ob=Solution()
        if(ob.find3Numbers(A,n,X)):
            print(1)
        else:
            print(0)
# } Driver Code Ends