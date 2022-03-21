class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        temp=[]
        result =[]
        for i in range(len(a)):
            temp.append(a[i])
        #code here
        for j in range(len(b)):
            temp.append(b[j])
        result=set(temp)
        return len(result)
