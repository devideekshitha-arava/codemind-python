from math import sqrt
n=int(input())
sq=int(sqrt(n))
if n==sq*sq:
    print(True)
else:
    print(False)