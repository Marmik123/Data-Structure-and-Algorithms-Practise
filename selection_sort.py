#SELECTION SORT 
class Solution: 
    def select(self, arr, i):
        # code here 
        min =arr[i]
        min_idx =i
        for j in range(i,len(arr)):
            if arr[j]<min:
                min=arr[j]
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]        
                
    
    def selectionSort(self, arr,n):
        #code here
        # sorted =[0]*n
        for i in range(len(arr)):
            self.select(arr,i)
            