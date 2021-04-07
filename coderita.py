for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    i=0
    while True:
        c+=1
        if i==(len(l)-1):
            i=0
        if l[i]==0:
            print(i+1)
            break
        else:
            i+=1
            l[i]=l[i]-c
