def factorial(n,res):
    if n==0:
        return res
    res=res*n
    return(factorial(n-1,res))

def nCr(n, r): 
    # code here
    res=1
    N=factorial(n,res)
    K=factorial(n-r,res)
    R=factorial(r,res)
    return (N//(K*R))    
n=int(input())
r=int(input())
print(nCr(n,r))
