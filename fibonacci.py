def fibonacci(num):
    A = [0]*(num+1)
    if num>1:
        A[0]=0
        A[1]=1 
        for i in range(2,(num+1)): 
            A[i] = A[i-1] + A[i-2]     
                   
        return A[num]   
    elif num==0:
        return 0
    elif num==1:
        return 1
    
    
# def fibo_naive(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     elif n>1:
#         return fibo_naive(n-1)+fibo_naive(n-2)

if __name__=='__main__':
    n = int(input(''))
    fib= fibonacci(n) 
    print(fib)
#     print(fib%10)