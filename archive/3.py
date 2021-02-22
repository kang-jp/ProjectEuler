from math import sqrt

n=600851475143
sup=int(sqrt(n))+1

def primeList(su):
    """N=su, O(NlogN)"""

    ret=[True for _ in range(su+1)]
    ret[0]=ret[1]=False
    k=2
    while k<=su:
        if ret[k]:
            for i in range(k*2,su+1,k):
                ret[i]=False
        k+=1
    return [i for i,b in enumerate(ret) if b]

pl=primeList(sup)

ans=None
for d in pl:
    if n%d==0:
        ans=d
print(ans)