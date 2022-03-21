class Solution:
    
    def mergeSort(self,arr):
        if len(arr)>1:
            m = len(arr)//2   #MID VALUE
            L=arr[:m]
            R=arr[m:]
            self.mergeSort(L)
            self.mergeSort(R)
            i=j=k=0
            while i<len(L) and j<len(R):
                if L[i]<R[j]:
                    arr[k]=L[i]
                    i+=1
                else:
                    arr[k]=R[j]
                    j+=1
                k+=1
            while i<len(L):
                arr[k]=L[i]
                i+=1
                k+=1
            while j<len(R):
                arr[k]=R[j]
                j+=1
                k+=1
                
        return arr 
        
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        
        
        
        # min=arr[0]
        if len(arr)==1:
            return arr[0]
        else:
            sorted=self.mergeSort(arr)
            return sorted[k-1]