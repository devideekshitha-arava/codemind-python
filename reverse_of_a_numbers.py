n=int(input())
rev_num=0
while(n>0):
    r=n%10
    rev_num=rev_num*10+r
    n=int(n/10)
print(rev_num)    