def power1(x,y):
    s=1
    for i in range y:
        s*=i
    return s


a=map(int,raw_input().strip().split(' '))
print(power1(int(a[0]),int(a[1])))

