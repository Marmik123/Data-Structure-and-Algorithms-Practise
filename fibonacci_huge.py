def huge_fibo(n,m):
    if n<=1:
        return n
    
    else :
        previous = 0
        current = 1 
        sum=1
        
        for _ in range(n-1):
            previous,current = current, previous+current
#             sum+=current
        return current%m   
    
if __name__=='__main__':
    n,m = [int(x) for x in input().split()]
    sum = huge_fibo(n,m)
    print(sum)