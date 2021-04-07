for i in range(int(input())):
    M,N=map(int,input().split())
    X,Y=map(int,input().split())
    rc=0
    cc=0
    if (M>=8 and M<=40) and (N>=8 and N<=40):
        if (X+1)<M:
            for f in range(Y+2):
                rc+=1
        if (Y+1)<N:
            if rc!=0:
                for f in range(X+2):
                    cc+=1
            else:
                for f in range(X+1):
                    cc+=1
        if ((X+1)<M) and cc==0:
            rc=0
            for f in range(Y+1):
                rc+=1
        if rc==0:
            print(cc)
        elif cc==0:
            print(rc)
        else:
            print((rc+cc)-1)
            
            
            
