import math
a=int(input())
b=int(input())
for x in range(a,b+1):
    sam=int(math.sqrt(x))
    if sam*sam==x:
        print(x)


