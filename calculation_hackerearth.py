def calcT(N):
    tn=[0]*N
    A=None
    tn[0]=3
    tn[1]=2
    tn[2]=1
    for i in range(3,len(tn)):
        tn[i]=tn[i-1]+tn[i-2]+tn[i-3]

    for i in range(len(tn)):
        if A!=None:
            A = A+(tn[i]*tn[i])
            # print(A)
        else:
            A=(tn[i]*tn[i])


    return A%(1e9+7)

if  __name__=='__main__':
    n = int(input())                  # Reading input from STDIN
    print(int(calcT(n))) 