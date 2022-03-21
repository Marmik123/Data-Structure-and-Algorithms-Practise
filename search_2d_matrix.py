class Solution(object):
                         
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m=len(matrix)
        for i in range(0,m):
            n = len(matrix[i])
            if matrix[i][n-1]>target:
                # print(matrix[i])
                # print(matrix[i][n-1])
                result=self.binarySearch(matrix[i],0,n-1,target)
                return result
                break
            elif matrix[i][n-1] == target:
                return True
            else:
                i+=1
              
    def binarySearch(self,arr,l,r,target):
        # print(l)
        # print(r)
        # print(target)
        # print(arr)
        if r>=l:
            mid = l+ (r-l) // 2
            if target == arr[mid]:
                return True
            elif target < arr[mid]:
                return self.binarySearch(arr,l,mid-1,target)
            else:
                return self.binarySearch(arr,mid+1,r,target)
        else: 
            return False         
