for _ in range(int(input())):
    m,n=map(int,input().split())
    matrix=[]
    s=0
    for h in range(m):
        k=list(map(int,input().split()))
        matrix.append(k)
    print(matrix)
    i=0
    while i<len(matrix):
        if i==len(matrix)-1:
            val=max(matrix[i])
        else:
            val=max(matrix[i])
            print(val,"value in else")
            d=matrix[i].index(val)
            print(d,"index value")
            print(matrix[i+1][d],"poping value")
            matrix[i+1].pop(d)
        s=s+val
        i+=1
    print(s)    
