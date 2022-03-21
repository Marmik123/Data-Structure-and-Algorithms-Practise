def fibonacci(num):
    A = [0]*(num+1)
    if num<=1:
        return num
    else:
        A[0]=0
        A[1]=1 
        for i in range(2,(num+1)): 
            A[i] = (A[i-1] + A[i-2])%10     
                   
        return A[num]   

if __name__=='__main__':
    m = int(input())
    last_digit = fibonacci(m)
    print(last_digit)
#     print(fib%10)