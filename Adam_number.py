n=int(input())
m=n*n
rev=0
rev2=0
while(n>0):
    r=n%10
    rev=rev*10+r
    n=int(n//10)
nrev=rev*rev
while(nrev>0):
    b=nrev%10
    rev2=rev2*10+b
    nrev=int(nrev//10)
if rev2==m:
    print(True)
else:
    print(False)
    