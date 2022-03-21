def sum_fibo_last(n):
    if n<=1:
        return n
    
    else :
        previous = 0
        current = 1 
        sum=1
        
        for _ in range(n-1):
            previous,current = current, previous+current
            sum+=current*current
        return sum%10   
    
if __name__=='__main__':
    n =  int(input())
    digit = sum_fibo_last(n)
    print(digit)