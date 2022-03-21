#User function Template for python3

class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
      
        temp=[]
        for i in range(len(arr)):
            if arr[i]>0:
                temp.append(arr[i])
                # print(temp)
        for i in range(len(arr)):
            if arr[i]<0:
                temp.append(arr[i])
                # print(temp)
        for i in range(len(arr)):
            arr[i]=temp[i]
        
                # p=arr.remove(arr[i])
                # print(p)
