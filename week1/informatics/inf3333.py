
x = int(raw_input().stip())
y = map(int, raw_input().strip().split(' '))
cnt=0
for i in range(x):
    if y[i]>y[i-1]:
        cnt+=1
print(cnt)
