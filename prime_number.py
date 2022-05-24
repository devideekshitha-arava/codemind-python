from math import *
def isprime(n):
    if n==0 or n==1:
        return false
    
    sqr=int(sqrt(n))
    for i in range(2,sqr+1):
        if n%i==0:
            return False
    return True    

n=int(input())
if isprime(n):
    print("prime")
else:
    print("not a prime")

