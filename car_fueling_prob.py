#FUNCTION FOR CAR FUELING PROBLEM
def c_fuel(x,n,L):
    cr_refill =0
    last_fill=0
    num_fill=0
    while cr_refill<=n:
        last_fill=cr_refill
        while cr_refill<=n and x[cr_refill+1] - x[last_fill]<=L:
            cr_refill+=cr_refill
        if cr_refill ==last_fill:
            return 'IMPOSSIBLE'
        if cr_refill<=n:
            num_fill+=num_fill
    return num_fill
    
if  __name__== '__main__':
    d = int(input())  #DISTANCE BETWEEN SOURCE A and DESTINATION B.
    L = int(input())  #MAXIMUM DISTANCE CAR CAN COVER.
    n = int(input())  #NO. OF STOPS.
    x = [int(x) for x in input().split()] #STOP LOCATIONS BY DISTANCE. 
    print(c_fuel(x,n,L))