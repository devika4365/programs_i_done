def f(u,s):
    if (u[0]+u[1])<=s:
        return u[0]*u[1]
    else:
        return 0
s=int(input())
u=list(map(int,input().split()))
u.sort()
d= f(u,s)
print(d)
