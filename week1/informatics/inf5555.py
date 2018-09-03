import math

x = int(raw_input().stip())
y = map(int, raw_input().strip().split(' '))
cnt=0
for i in range(1,x):
    if y[i]>=0 and y[i-1]>=0 or y[i]<0 and y[i-1<0]:
        print('YES')
        break
    print('NO')

