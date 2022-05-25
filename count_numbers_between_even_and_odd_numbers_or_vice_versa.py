n=int(input())
l=list(map(int,input().split()))
o=0
for i in range(0,len(l)-2):
    if l[i]%2==0 and l[i+2]%2!=0:
        o+=1
    elif l[i]%2!=0 and l[i+2]%2==0:
        o+=1
    
print(o)
        