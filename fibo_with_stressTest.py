import random
def huge_fibo(n,m):
    if n<=1:
        return n
    else :
        previous = 0
        current = 1 
        sum=1
        
        for _ in range(n-1):
            previous,current = current, previous+current
            sum+=current
        return current%m   

def fibo_naive(n,m):
    if n<=1:
        return n
    else:
        fibo=fibo_naive(n-1,m)+fibo_naive(n-2,m)
    return fibo%m
    print('fibo_naive')
    
def stressTest(n,M):
    while 'true':        
        num = random.randint(0,n)
        res1 = fibo_naive(num,M)
        res2 = huge_fibo(num,M)
        if(res1==res2):
            print('OK')
        else:
            print('Wrong ANSWER',res1,res2)
            
    
    

if __name__=='__main__':
    n,m = [int(x) for x in input().split()]
    stressTest(n,m)