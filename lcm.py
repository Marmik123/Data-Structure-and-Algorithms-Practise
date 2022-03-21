def gcd(a,b):
    if b==0:
        return a
    elif a==0:
        return b
    else:
        a_prime = a%b 
        return gcd(b,a_prime)

def lcm(a,b):
    prod = a*b 
    ans = gcd(a,b)
    return int(prod/ans)

if __name__=='__main__':
    a,b = map(int,input().split())
#     ans = gcd(a,b)
    lcm_ans  = lcm(a,b)
    print(lcm_ans)