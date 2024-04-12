class Solution 
{ 
    static void swap(int[] arr,int i, int j){
        int temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
    }
    public static int partition(int[] arr,int low,int high){
        int pivot=arr[high];
        int i=low-1;
        for(int j=low;j<high;j++){
            if(arr[j]<pivot){
                i++;
                swap(arr,i,j);
            }
        }
        i++;
        swap(arr,i,high);
        return i;
    }
    public static void quickSort(int[] arr, int start , int end){
        if(end<=start)    return;
        int pivot=partition(arr,start,end);
        quickSort(arr,start,pivot-1);
        quickSort(arr,pivot+1,end);
        
    }
    
    int[] sortArr(int[] arr, int n) 
    { 
        // code here
        quickSort(arr,0,n-1);
        return arr;
    }
} 
