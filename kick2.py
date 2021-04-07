t = int(input())
for j in range(t):
    d,n = map(int,input().split())
    l=list(map(int,input().split()))
    l[len(l) - 1] = l[len(l) - 1] * (n // l[len(l) - 1])
    print(l[len(l) - 1],l[len(l) - 1] * (n // l[len(l) - 1]))
    for i in reversed(range(len(l) - 1)):
        l[i] = l[i] * (l[i + 1] // l[i])
        print(l[i])
    print("case #{0}: {1}".format(j + 1,min(l)))
