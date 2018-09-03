x = int(raw_input().stip())
y = map(int, raw_input().strip().split(' '))

for i in range(x):
    if y[i] % 2 == 0:
        print(y[i])


