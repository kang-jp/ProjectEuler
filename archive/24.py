from mylib.operators import fact

def f(L,R,div,tgt,S=set('0123456789')):
    num=sorted(list(S))
    if div==0: return ''
    unit=(R-L)//div
    for k in range(0,div+1):
        l=L+unit*k
        r=L+unit*(k+1)
        if l<=tgt<r:
            return num[k]+f(l,r,div-1,tgt,S=S-{num[k]})
    
print(f(1,fact(10)+1,10,10**6))

