import math

x = int(raw_input().stip())
y = map(int, raw_input().strip().split(' '))
cnt=0
for i in range(1,x-1):
    if y[i]>y[i-1] and y[i]>y[i+1]:
        cnt+=1
print(cnt)

