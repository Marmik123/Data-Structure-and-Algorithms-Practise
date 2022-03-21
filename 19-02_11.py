#User function Template for python3
#ALTERNATE POSITIVE AND NEGATIVE NUMBERS.
class Solution:
    def rearrange(self,arr, n):
        # code here
        pos=[]
        neg=[]
        result=[]
        for i in range(n):
            if arr[i]<0:
                neg.append(arr[i])
        # print(neg)            
        for i in range(n):
            if arr[i]>=0:
                pos.append(arr[i])

        # print(pos)
        for i in range(n):
            if i<len(pos):
                result.append(pos[i])
                   
            if i<len(neg):
                result.append(neg[i])
             
        for i in range(n):
            arr[i]=result[i]
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.rearrange(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1

# } Driver Code Ends