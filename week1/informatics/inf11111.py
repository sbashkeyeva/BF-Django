def minim(s):
    mini = 999999
    for i in s:
        if i < mini:
            mini = i
            return mini


inp = map(int, raw_input().strip().split(' '))
print(minim(inp))

