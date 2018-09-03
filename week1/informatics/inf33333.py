def boolxor(x,y):
    if x==y:
        return(0)
    else:
        return(1)


a=map(int,raw_input().strip().split(' '))
print(boolxor(a[0],a[1]))

