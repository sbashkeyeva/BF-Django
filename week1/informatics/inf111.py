import math
x=input()
i=1
while i<=x:
    s=int(math.sqrt(i*i))
    if(s*s==i):
        print(i)
    i+=1
