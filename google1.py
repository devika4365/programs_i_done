t=int(input())
for i in range(t):
    n=int(input())
    v=list(map(int,input().split()))
    out=0
    max_ele=-1
    for j in range(n):
        if v[j]>max_ele:
            max_ele=v[j]
            if j==n-1 or v[j]>v[j+1]:
                out+=1
    print("case #"+str(i+1)+': '+str(out))            
