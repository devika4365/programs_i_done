def nearest(n):
    while True:
        rev=int(str(n)[::-1])
        if rev==n:
            return int(n)
        n+=1
n=int(input())
#nearest(n)
print(nearest(n))
