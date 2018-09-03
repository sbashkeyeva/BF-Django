if __name__ == '__main__':
    N=int(raw_input())
    list=[]
    for i in range(N):
        output1=raw_input().split()
        if output1[0]=='print':
            print(list)
        elif output1[0]=='sort':
            list.sort()
        elif output1[0]=='insert':
            list.insert(int(output1[1]),int(output1[2]))
        elif output1[0]=='append':
            list.append(int(output1[1]))
        elif output1[0]=='reverse':
            list.reverse()
        elif output1[0]=='remove':
            list.remove(int(output1[1]))
        elif output1[0]=='pop':
            list.pop()

