import random

def max_pairwise(num):
    n = len(num)
    max_index = 0
    max_index2 = 0
    for i in range (1,n):
        if num[i]>num[max_index]:
            max_index = i
    #SWAP        
    x= num[n-1]
    num[n-1] = num[max_index]
    num[max_index]=x
    
    for j in range (1,n-1):
        if num[j]>num[max_index2]:
            max_index2=j
    #SWAP
    y= num[n-2]
    num[n-2] = num[max_index2]
    num[max_index2]=y
#     num[n-2],num[max_index2] = num[max_index2],num[n-2]
    print(num[n-1]*num[n-2])
    
    
# def max_p_naive(num,n):
#     max_product =0
#     for i in range (n):
#         for j in range(i+1,n):
#             max_product = max(max_product,num[i]*num[j])
#     print(max_product)  
    
# def stress_test(N,M):
#     print('sTRESS TEST CALLED')
#     while 'true':
#         n = random.randint(1,N)
#         #allocate array
#         A = [random.randint(0,M) for x in range(n)]
#         result_naive = max_p_naive(A,n)
#         result_fast = max_pairwise(A)
#         if(result_naive == result_fast):
#             print('OK')
#         else:
#             print('WRONG ANSWER',result_naive,result_fast)
#             return 
        
if __name__ == '__main__':
    n = int(input())
    A = [int(x) for x in input().split()]
    max_pairwise(A)
#        
#     stress_test(5,9)   
