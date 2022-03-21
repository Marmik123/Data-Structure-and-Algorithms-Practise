#COMPARE IN PAIRS APPROACH.(USED TO REDUCED NUMBER OF COMPARISONS.)
import random
def minMax(arr,n):
    min=0
    max=0
    i=0
    #If n is even.
    if n%2==0:
        if arr[0]>arr[1]:
            max = arr[0]
            min = arr[1]
        else:
            max = arr[1]
            min = arr[0]

        i=2
    #if n is odd.    
    else:
        min = arr[0]
        max = arr[0]

    while i<n-1:
        if arr[i]>arr[i+1]:
            if arr[i]>max:
                max = arr[i]
            if arr[i+1]<min:
                min = arr[i+1]
        if arr[i+1]>arr[i]:
            if arr[i+1]>max:
                max = arr[i+1]
            if arr[i]<min:
                min = arr[i]        
        i+=2        
    return min,max

if __name__ == '__main__':
    n = int(input('enter size of an array'))
    arr = [int(x) for x in input('Enter elements').split()]
    """ n = int(random.randint(1,500))
    arr = [random.randrange(0,1000,1) for i in range(n)]
     """
    print(n)
    print(arr)
    
    min,max = minMax(arr,n)
    print('minimun and maximum is',min,max,'respectively')
    
    

